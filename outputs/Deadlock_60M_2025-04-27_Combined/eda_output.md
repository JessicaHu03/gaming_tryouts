# Starting EDA for Deadlock 60M 2025-04-27 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 459 entries, 0 to 458
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              459 non-null    object 
    1   Start Time           459 non-null    int64  
    2   End Time             459 non-null    int64  
    3   IO Time              459 non-null    int64  
    4   Disk SrvT            459 non-null    int64  
    5   IO Size              459 non-null    int64  
    6   Byte Offset          459 non-null    int64  
    7   Pri                  459 non-null    int64  
    8   QD/I                 459 non-null    int64  
    9   QD/C                 459 non-null    int64  
    10  IBCB                 459 non-null    int64  
    11  IBCA                 459 non-null    int64  
    12  IACB                 459 non-null    int64  
    13  Process Name ( PID)  459 non-null    object 
    14  Disk                 459 non-null    int64  
    15  Filename             459 non-null    object 
    16  Process Name         459 non-null    object 
    17  PID                  459 non-null    int64  
    18  Duration_s           459 non-null    float64
    19  Throughput_MB_s      459 non-null    float64
    20  Throughput_GB_s      459 non-null    float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 75.4+ KB
   

## Processed Data Description
|       |    Start Time |      End Time |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |       QD/I |       QD/C |       IBCB |       IBCA |       IACB |   Disk |      PID |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|--------------:|--------------:|----------:|------------:|-----------------:|--------------:|------:|-----------:|-----------:|-----------:|-----------:|-----------:|-------:|---------:|--------------:|------------------:|------------------:|
| count | 459           | 459           |    459    |      459    |    459           | 459           |   459 | 459        | 459        | 459        | 459        | 459        |    459 |   459    | 459           |     459           |        459        |
| mean  |   1.33383e+09 |   1.33383e+09 |   2894.99 |     1946.4  |      1.23996e+06 |   1.73762e+11 |     3 |   0.640523 |   0.640523 |   0.496732 |   0.143791 |   0.154684 |      0 | 27787.6  |   2.89499e-06 |       1.28273e+06 |       1252.67     |
| std   |   8.39295e+08 |   8.39295e+08 |   3402.15 |     3070.17 | 565510           |   3.69767e+10 |     0 |   1.11136  |   1.10939  |   0.947008 |   0.429557 |   0.481123 |      0 |  7485.51 |   3.40215e-06 |       1.04228e+06 |       1017.85     |
| min   |   3.09935e+07 |   3.09942e+07 |      9    |        1    |   1536           |   3.23651e+09 |     3 |   0        |   0        |   0        |   0        |   0        |      0 |     4    |   9e-09       |     999.169       |          0.975751 |
| 25%   |   4.6457e+08  |   4.6457e+08  |    552.5  |      149    |      1.04858e+06 |   1.75343e+11 |     3 |   0        |   0        |   0        |   0        |   0        |      0 | 29800    |   5.525e-07   |  157628           |        153.934    |
| 50%   |   1.30731e+09 |   1.30731e+09 |    797    |      485    |      1.04858e+06 |   1.80854e+11 |     3 |   0        |   0        |   0        |   0        |   0        |      0 | 29800    |   7.97e-07    |       1.32802e+06 |       1296.9      |
| 75%   |   2.00078e+09 |   2.00078e+09 |   7848.5  |      854.5  |      2.09715e+06 |   1.88326e+11 |     3 |   1        |   1        |   1        |   0        |   0        |      0 | 29800    |   7.8485e-06  |       2.06718e+06 |       2018.73     |
| max   |   2.7539e+09  |   2.7539e+09  |   9900    |     8836    |      2.09715e+06 |   2.59359e+11 |     3 |   7        |   7        |   7        |   3        |   5        |      0 | 29800    |   9.9e-06     |       4.37637e+06 |       4273.8      |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |       QD/I |       QD/C |       IBCB |       IBCA |       IACB |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|--------------:|------:|-----------:|-----------:|-----------:|-----------:|-----------:|--------------:|------------------:|------------------:|
| count |    459    |      459    |    459           | 459           |   459 | 459        | 459        | 459        | 459        | 459        | 459           |     459           |        459        |
| mean  |   2894.99 |     1946.4  |      1.23996e+06 |   1.73762e+11 |     3 |   0.640523 |   0.640523 |   0.496732 |   0.143791 |   0.154684 |   2.89499e-06 |       1.28273e+06 |       1252.67     |
| std   |   3402.15 |     3070.17 | 565510           |   3.69767e+10 |     0 |   1.11136  |   1.10939  |   0.947008 |   0.429557 |   0.481123 |   3.40215e-06 |       1.04228e+06 |       1017.85     |
| min   |      9    |        1    |   1536           |   3.23651e+09 |     3 |   0        |   0        |   0        |   0        |   0        |   9e-09       |     999.169       |          0.975751 |
| 25%   |    552.5  |      149    |      1.04858e+06 |   1.75343e+11 |     3 |   0        |   0        |   0        |   0        |   0        |   5.525e-07   |  157628           |        153.934    |
| 50%   |    797    |      485    |      1.04858e+06 |   1.80854e+11 |     3 |   0        |   0        |   0        |   0        |   0        |   7.97e-07    |       1.32802e+06 |       1296.9      |
| 75%   |   7848.5  |      854.5  |      2.09715e+06 |   1.88326e+11 |     3 |   1        |   1        |   1        |   0        |   0        |   7.8485e-06  |       2.06718e+06 |       2018.73     |
| max   |   9900    |     8836    |      2.09715e+06 |   2.59359e+11 |     3 |   7        |   7        |   7        |   3        |   5        |   9.9e-06     |       4.37637e+06 |       4273.8      |

### IOPS and Throughput Calculations

Total duration of the session: 2.72 seconds

IOPS per disk
|   Disk |      0 |
|-------:|-------:|
|      0 | 168.57 |

IOPS per IO type
| IO Type   |         0 |
|:----------|----------:|
| Diskread  | 158.654   |
| Diskwrite |   9.91586 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.28273e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.34624e+06 |
| Diskwrite |  266695           |

## Visualizations

### IOPS per Disk and IO Type
![IOPS](images\iops_by_disk_and_type.png)

### Average Throughput per Disk and IO Type
![Throughput](images\Throughput_by_disk_and_type.png)

# Generating Visualizations

## Univariate Analysis

### Numerical Features Distribution

#### Log Transformations for skewed distributions
![Key Metric (Log) Distributions](images\key_metric_distributions.png)

#### Boxplots to Identify Outliers
![Boxplots to Identify Outliers](images\Boxplots_outliers.png)

#### Log-Normal Distribution Fit for IO Time
![Log-Normal Distribution Fit for IO Time](images\lognormal_io_time.png)
Log-Normal Fit Parameters for IO Time: (0, 0, 6)

### Categorical Features Distribution

#### Value Counts for Categorical Features

Value Counts for IO Type:
| IO Type   |   count |
|:----------|--------:|
| Diskread  |     432 |
| Diskwrite |      27 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |     459 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

