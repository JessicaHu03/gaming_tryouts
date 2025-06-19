import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import scipy.stats as stats

def perform_eda(df, session_name, output_dir):
    """
    Performs EDA on the given DataFrame, saves outputs directly to a Markdown file,
    and saves images to an images subfolder with links in the Markdown.
    """
    # Create output directory and images subfolder
    os.makedirs(output_dir, exist_ok=True)
    images_dir = os.path.join(output_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    # Open Markdown file for writing
    markdown_file = os.path.join(output_dir, 'eda_output.md')
    
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(f"# Starting EDA for {session_name}\n\n")

        # --- Data Processing ---
        # Clean and standardize IO Type
        df['IO Type'] = df['IO Type'].str.strip().str.lower().str.capitalize()

        # Convert hexadecimal columns to integers
        df['IO Size'] = df['IO Size'].apply(lambda x: int(x, 16))
        df['Byte Offset'] = df['Byte Offset'].apply(lambda x: int(x, 16))

        # Extract Process Name and PID
        df[['Process Name', 'PID']] = df['Process Name ( PID)'].str.extract(r'(.+)\s*\(\s*(\d+)\)')
        df['PID'] = pd.to_numeric(df['PID'], errors='coerce')

        # --- Feature Engineering ---
        # f.write("Performing feature engineering...\n")
        df['Duration_s'] = df['IO Time'] / 1_000_000_000  # Convert nanoseconds to seconds
        df['Throughput_MB_s'] = (df['IO Size'] / (1024 * 1024)) / (df['Duration_s'])
        df.loc[(df['Duration_s'] == 0) | (df['Throughput_MB_s'] == np.inf), 'Throughput_MB_s'] = 0

        # --- Initial Data Overview ---
        f.write("# Processed Data Overview\n\n")

        # Capture df.info() output
        from io import StringIO
        info_buffer = StringIO()
        df.info(buf=info_buffer)
        f.write("## Processed Data Info\n")
        f.write(info_buffer.getvalue().replace("\n", "\n   ") + "\n\n")
        info_buffer.close()

        # Capture df.describe() output as a Markdown table
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
            desc_table = df.describe().to_markdown()
        f.write("## Processed Data Description\n")
        f.write(desc_table + "\n\n")

        cols = ['IO Time', 'Disk SrvT', 'IO Size', 'Byte Offset', 'Pri', 'QD/I', 'QD/C', 
                'IBCB', 'IBCA', 'IACB', 'Duration_s', 'Throughput_MB_s', 'Throughput_GB_s']
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
            desc_selected_table = df[cols].describe().to_markdown()
        f.write("## Description of Selected Columns\n")
        f.write(desc_selected_table + "\n\n")

        # Missing Values
        # f.write("## Missing Values after Processing\n")
        # f.write(df.isnull().sum().to_markdown() + "\n\n")

        # Convert nanoseconds to seconds (global duration)
        f.write("### IOPS and Throughput Calculations\n\n")
        total_duration_sec = (df['End Time'].max() - df['Start Time'].min()) / 1e9
        f.write(f"Total duration of the session: {total_duration_sec:.2f} seconds\n\n")

        # Group by disk and count IOs
        iops_per_disk = df.groupby('Disk').size() / total_duration_sec
        f.write("IOPS per disk\n")
        f.write(iops_per_disk.to_markdown() + "\n\n")

        # Group by IO type and count IOs
        iops_per_io_type = df.groupby('IO Type').size() / total_duration_sec
        f.write("IOPS per IO type\n")
        f.write(iops_per_io_type.to_markdown() + "\n\n")

        # Group by disk and calculate average throughput
        avg_mb_throughput_per_disk = df.groupby('Disk')['Throughput_MB_s'].mean()
        f.write("Average throughput per disk (MB/s)\n")
        f.write(avg_mb_throughput_per_disk.to_markdown() + "\n\n")

        # Group by IO type and calculate average throughput
        avg_mb_throughput_per_io_type = df.groupby('IO Type')['Throughput_MB_s'].mean()
        f.write("Average throughput per IO type (MB/s)\n")
        f.write(avg_mb_throughput_per_io_type.to_markdown() + "\n\n")

        # Set style
        f.write("## Visualizations\n\n")
        sns.set(style="whitegrid")

        # === IOPS per Disk and IO Type ===

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # IOPS per Disk
        iops_per_disk = df.groupby('Disk').size() / total_duration_sec
        axes[0].bar(iops_per_disk.index.astype(str), iops_per_disk.values, color='skyblue')
        axes[0].set_title('IOPS per Disk')
        axes[0].set_xlabel('Disk')
        axes[0].set_ylabel('IOPS')

        # IOPS per IO Type
        iops_per_io_type = df.groupby('IO Type').size() / total_duration_sec
        axes[1].bar(iops_per_io_type.index, iops_per_io_type.values, color='salmon')
        axes[1].set_title('IOPS per IO Type')
        axes[1].set_xlabel('IO Type')
        axes[1].set_ylabel('IOPS')

        plt.tight_layout()
        iops_img_path = os.path.join(images_dir, 'iops_by_disk_and_type.png')
        plt.savefig(iops_img_path, dpi=300)
        plt.close()
        f.write("### IOPS per Disk and IO Type\n")
        f.write(f"![IOPS](images\iops_by_disk_and_type.png)\n\n")

        # === Average Throughput per Disk and IO Type ===
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Avg Throughput per Disk
        avg_mb_throughput_per_disk = df.groupby('Disk')['Throughput_MB_s'].mean()
        axes[0].bar(avg_mb_throughput_per_disk.index.astype(str), avg_mb_throughput_per_disk.values, color='mediumseagreen')
        axes[0].set_title('Avg Throughput per Disk (MB/s)')
        axes[0].set_xlabel('Disk')
        axes[0].set_ylabel('MB/s')

        # Avg Throughput per IO Type
        avg_mb_throughput_per_io_type = df.groupby('IO Type')['Throughput_MB_s'].mean()
        axes[1].bar(avg_mb_throughput_per_io_type.index, avg_mb_throughput_per_io_type.values, color='orchid')
        axes[1].set_title('Avg Throughput per IO Type (MB/s)')
        axes[1].set_xlabel('IO Type')
        axes[1].set_ylabel('MB/s')

        plt.tight_layout()
        throughput_img_path = os.path.join(images_dir, 'Throughput_by_disk_and_type.png')
        plt.savefig(throughput_img_path, dpi=300)
        plt.close()
        f.write("### Average Throughput per Disk and IO Type\n")
        f.write(f"![Throughput](images\Throughput_by_disk_and_type.png)\n\n")

        #######################################

        # --- Exploratory Visualizations ---
        f.write("# Generating Visualizations\n\n")
        
        # Key Metric Distributions
        num_cols = ['IO Time', 'Disk SrvT', 'IO Size', 'Duration_s', 'Throughput_MB_s',  'QD/C']
        cat_cols = ['IO Type', 'Disk', 'Filename', 'Process Name']

        f.write("## Univariate Analysis\n\n")
        f.write("### Numerical Features Distribution\n\n")

        f.write("#### Log Transformations for skewed distributions\n")
        df['Log IO Size'] = np.log1p(df['IO Size'])
        df['Log IO Time'] = np.log1p(df['IO Time'])
        df['Log Disk SrvT'] = np.log1p(df['Disk SrvT'])
        df['Log Duration_s'] = np.log1p(df['Duration_s']) 
        df['Log Throughput_MB_s'] = np.log1p(df['Throughput_MB_s'])
        df['Log QD/C'] = np.log1p(df['QD/C'])

        sns.set_style("whitegrid")

        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle(f'Key Metric Distributions for {session_name}', fontsize=16)

        sns.histplot(df['Log IO Time'], bins=50, kde=True, ax=axes[0, 0])
        axes[0, 0].set_title('Distribution of Log IO Time (ns)')
        axes[0, 0].set_xlabel('Log IO Time (ns)')

        sns.histplot(df['Log Disk SrvT'], bins=50, kde=True, ax=axes[0, 1])
        axes[0, 1].set_title('Distribution of Disk Service Time (ns)')
        axes[0, 1].set_xlabel('Log Disk Service Time (ns)')

        sns.histplot(df['Log IO Size'] / 1024, bins=50, kde=True, ax=axes[0, 2])
        axes[0, 2].set_title('Distribution of Log IO Size (KB)')
        axes[0, 2].set_xlabel('Log IO Size (KB)')

        sns.histplot(df['Log Duration_s'], bins=50, kde=True, ax=axes[1, 0])
        axes[1, 0].set_title('Distribution of Log I/O Duration (s)')
        axes[1, 0].set_xlabel('Log I/O Duration (s)')

        sns.histplot(df['Log Throughput_MB_s'], bins=50, kde=True, ax=axes[1, 1])
        axes[1, 1].set_title('Distribution of Log Throughput (MB/s)')
        axes[1, 1].set_xlabel('Log Throughput (MB/s)')

        sns.histplot(df['Log QD/C'], bins=30, kde=True, ax=axes[1, 2])
        axes[1, 2].set_title('Distribution of Log Current Queue Depth (QD/C)')
        axes[1, 2].set_xlabel('Log Queue Depth')

        plt.tight_layout(rect=[0, 0.03, 1, 0.96])
        image_path = os.path.join(images_dir, 'key_metric_distributions.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Key Metric (Log) Distributions](images\key_metric_distributions.png)\n\n")


        f.write("#### Boxplots to Identify Outliers\n")
        outlier_cols = ['Throughput_MB_s', 'IO Size', 'Disk SrvT']
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle('Boxplots to Identify Outliers', fontsize=16)
        for ax, col in zip(axes, outlier_cols):
            sns.boxplot(data=df, y=col, ax=ax)
            ax.set_title(f'Outliers in {col}')
            ax.set_ylabel(col)
        plt.tight_layout()
        image_path = os.path.join(images_dir, 'Boxplots_outliers.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Boxplots to Identify Outliers](images\Boxplots_outliers.png)\n\n")

        f.write("#### Log-Normal Distribution Fit for IO Time\n")
        io_time_log = df['Log IO Time'].dropna()
        params = stats.lognorm.fit(io_time_log, floc=0)
        x = np.linspace(io_time_log.min(), io_time_log.max(), 100)
        pdf = stats.lognorm.pdf(x, *params)
        plt.figure(figsize=(8, 6))
        plt.hist(io_time_log, bins=50, density=True, alpha=0.5, label='Histogram')
        plt.plot(x, pdf, 'r-', lw=2, label='Log-Normal Fit')
        plt.title('Log-Normal Distribution Fit for IO Time')
        plt.xlabel('Log(IO Time + 1)')
        plt.ylabel('Density')
        plt.legend()
        image_path = os.path.join(images_dir, 'lognormal_io_time.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Log-Normal Distribution Fit for IO Time](images\lognormal_io_time.png)\n")
        f.write(f"Log-Normal Fit Parameters for IO Time: {tuple(int(x) for x in params)}\n\n")

        f.write("### Categorical Features Distribution\n\n")
        f.write("#### Value Counts for Categorical Features\n\n")
        categorical_cols = ['IO Type', 'Disk', 'Filename', 'Process Name']
        for col in categorical_cols:
            if col == 'Filename' or col == 'Process Name':
                continue
            f.write(f"Value Counts for {col}:\n")
            f.write(df[col].value_counts().to_markdown() + "\n\n")

        # Pie Charts for Categorical Variables
        f.write("#### Pie Charts for Categorical Variables\n")
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Pie Charts of Categorical Variables', fontsize=16)
        axes = axes.flatten()
        for i, col in enumerate(categorical_cols):
            plot_data = df.copy()
            if col == 'Filename':
                plot_data['Filename'] = plot_data['Filename'].str.slice(0, 15) + '...'
            pie_data = plot_data[col].value_counts()
            axes[i].pie(
                pie_data, 
                labels=pie_data.index, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=sns.color_palette("Pastel1")
            )
            axes[i].set_title(f'{col}', fontsize=12)
            axes[i].axis('equal')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        image_path = os.path.join(images_dir, 'categorical_pie_charts.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)\n\n")
        
        # Bivariate Analysis
        f.write("### Bivariate Analysis\n\n")
        f.write("#### Performance Metrics by IO Type\n")
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle(f'Performance Metrics by IO Type for {session_name}', fontsize=16)
        sns.boxplot(x='IO Type', y='IO Time', data=df, ax=axes[0], palette='pastel')
        axes[0].set_title('IO Time by IO Type')
        axes[0].set_ylabel('IO Time (ns)')
        sns.boxplot(x='IO Type', y='Disk SrvT', data=df, ax=axes[1], palette='pastel')
        axes[1].set_title('Disk Service Time by IO Type')
        axes[1].set_ylabel('Disk Service Time (ns)')
        plt.tight_layout(rect=[0, 0.03, 1, 0.96])
        image_path = os.path.join(images_dir, 'performance_metrics_by_io_type.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)\n\n")

        # IO Time per IO Type per Disk
        g = sns.catplot(
            x='IO Type', y='IO Time', col='Disk',
            data=df, kind='box', col_wrap=3,
            hue='IO Type', legend=False,
            palette='pastel', height=4, aspect=1
        )
        g.fig.suptitle(f'IO Time per IO Type per Disk for {session_name}', y=1.05)
        image_path = os.path.join(images_dir, 'io_time_per_io_type_per_disk.png')
        g.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)\n\n")

        # IO Size vs. Duration Log-Log Regression
        f.write("#### IO Size vs. IO Time Log-Log Regression\n")
        g = sns.lmplot(
            data=df,
            x='IO Size',
            y='IO Time',
            hue='Disk',
            logx=True,
            scatter_kws={'alpha':0.5},
            height=6,
            aspect=1.2
        )
        plt.yscale('log')
        plt.title('Log-Log Regression: IO Size vs Duration, Colored by Disk')
        plt.xlabel('IO Size (log scale)')
        plt.ylabel('IO Time (log scale)')
        plt.tight_layout()
        image_path = os.path.join(images_dir, 'io_size_vs_duration_loglog.png')
        g.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)\n\n")

        # # Disk ID Ratio and Service Time Ratio (Timeout)
        # f.write("#### Disk ID Ratio and Service Time Ratio\n")
        # # disk_counts = df['Disk'].value_counts()
        # io_time_log = df['Log IO Time'].dropna()
        # srv_time_per_disk = df.groupby('Disk')['Disk SrvT'].sum()
        # disk_ids = sorted(set(io_time_log.index).union(srv_time_per_disk.index))
        # # io_time_log = io_time_log.reindex(disk_ids, fill_value=0)
        # srv_time_per_disk = srv_time_per_disk.reindex(disk_ids, fill_value=0)

        # cmap = plt.cm.coolwarm
        # colors = [cmap(i / len(disk_ids)) for i in range(len(disk_ids))]

        # fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        # axes[0].pie(io_time_log, labels=None, autopct='%1.1f%%', startangle=90, colors=colors)
        # axes[0].set_title(f'Disk ID Ratio for {session_name}')
        # axes[0].axis('equal')
        # axes[1].pie(srv_time_per_disk, labels=None, autopct='%1.1f%%', startangle=90, colors=colors)
        # axes[1].set_title(f'Disk Service Time Ratio for {session_name}')
        # axes[1].axis('equal')
        # fig.legend(labels=[f'Disk {disk_id}' for disk_id in disk_ids],
        #            loc='center right', bbox_to_anchor=(1.1, 0.5))
        # plt.tight_layout()
        # image_path = os.path.join(images_dir, 'disk_id_ratio.png')
        # plt.savefig(image_path, dpi=300, bbox_inches='tight')
        # plt.close()
        # f.write(f"![Disk ID Ratio and Service Time Ratio](images\disk_id_ratio.png)\n\n")

        # Correlation heatmap
        numerical_cols = ['Duration_s', 'IO Time', 'IO Size', 'Disk SrvT', 'Throughput_MB_s']
        corr_matrix = df[numerical_cols].corr(numeric_only=True)
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap of Key Metrics')
        image_path = os.path.join(images_dir, 'correlation_heatmap.png')
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()
        f.write(f"![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)\n\n")

if __name__ == "__main__":
    dataset_path = '/mnt/shared/datasets/game-traces/processed_data/'
    output_path = '/home/appliedai/jessica/gaming_tryouts/outputs/'
    os.makedirs(output_path, exist_ok=True)

    files = [
        "cyberpunk_2077_combined.parquet", "deadlock_60m_2025-04-27_combined.parquet",
        "deadlock_60m_2025-04-28_combined.parquet", "deadlock_60m_2025-04-29_combined.parquet",
        "deadlock_60m_2025-05-01_combined.parquet", "deadlock_60m_2025-05-02_combined.parquet",
        "deadlock_60m_2025-05-03_combined.parquet", "deadlock_60m_2025-05-04_combined.parquet",
        "deadlock_60m_2025-05-05_combined.parquet", "deadlock_60m_2025-05-06_combined.parquet",
        "hogwarts_legacy_combined.parquet", "marvel_rivals_60m_2025-05-06_combined.parquet",
        "overwatch_60m_2025-04-28_combined.parquet", "the_finals_30m_2025-05-01_combined.parquet",
        "the_last_of_us_part_i.parquet"
    ]

    # for file in files:
    #     file_path = os.path.join(dataset_path, file)
    #     if os.path.exists(file_path):
    #         # Derive session_name from filename (remove .parquet and replace underscores with spaces)
    #         session_name = file.replace(".parquet", "").replace("_", " ").title()
    #         df = pd.read_parquet(file_path)
    #         output_dir = os.path.join(output_path, session_name.replace(" ", "_"))
    #         os.makedirs(output_dir, exist_ok=True)
    #         perform_eda(df, session_name, output_dir)
    #     else:
    #         print(f"File not found: {file_path}")

    file = "combined_deadlock.parquet"
    file_path = os.path.join(dataset_path, file)
    if os.path.exists(file_path):
        # Derive session_name from filename (remove .parquet and replace underscores with spaces)
        session_name = file.replace(".parquet", "").replace("_", " ").title()
        df = pd.read_parquet(file_path)
        output_dir = os.path.join(output_path, session_name.replace(" ", "_"))
        os.makedirs(output_dir, exist_ok=True)
        perform_eda(df, session_name, output_dir)
    else:
        print(f"File not found: {file_path}")