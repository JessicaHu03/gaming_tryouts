# Starting EDA for Deadlock 60M 2025-05-06 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 774 entries, 0 to 773
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              774 non-null    object 
    1   Start Time           774 non-null    int64  
    2   End Time             774 non-null    int64  
    3   IO Time              774 non-null    int64  
    4   Disk SrvT            774 non-null    int64  
    5   IO Size              774 non-null    int64  
    6   Byte Offset          774 non-null    int64  
    7   Pri                  774 non-null    int64  
    8   QD/I                 774 non-null    int64  
    9   QD/C                 774 non-null    int64  
    10  IBCB                 774 non-null    int64  
    11  IBCA                 774 non-null    int64  
    12  IACB                 774 non-null    int64  
    13  Process Name ( PID)  774 non-null    object 
    14  Disk                 774 non-null    int64  
    15  Filename             774 non-null    object 
    16  Process Name         774 non-null    object 
    17  PID                  774 non-null    int64  
    18  Duration_s           774 non-null    float64
    19  Throughput_MB_s      774 non-null    float64
    20  Throughput_GB_s      774 non-null    float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 127.1+ KB
   

## Processed Data Description
|       |    Start Time |      End Time |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |        IBCA |        IACB |   Disk |     PID |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|--------------:|--------------:|----------:|------------:|-----------------:|--------------:|------:|------------:|------------:|------------:|------------:|------------:|-------:|--------:|--------------:|------------------:|------------------:|
| count | 774           | 774           |   774     |     774     |    774           | 774           |   774 | 774         | 774         | 774         | 774         | 774         |    774 |   774   | 774           |     774           |         774       |
| mean  |   2.00339e+07 |   2.00342e+07 |   259.172 |     236.764 | 203666           |   3.29695e+11 |     3 |   0.0413437 |   0.0439276 |   0.0284238 |   0.0129199 |   0.0335917 |      0 | 23250.3 |   2.59172e-07 |       2.55077e+06 |        2490.98    |
| std   |   7.71413e+06 |   7.71435e+06 |   903.308 |     825.96  | 105024           |   1.1777e+11  |     0 |   0.353649  |   0.345936  |   0.303866  |   0.168206  |   0.430299  |      0 | 10958.4 |   9.03308e-07 |       1.53451e+06 |        1498.54    |
| min   |   8.3025e+06  |   8.3028e+06  |    11     |       0     |   1024           |   2.70521e+09 |     3 |   0         |   0         |   0         |   0         |   0         |      0 |     4   |   1.1e-08     |     530.524       |           0.51809 |
| 25%   |   1.71164e+07 |   1.71164e+07 |    68     |      68     |  65536           |   1.9018e+11  |     3 |   0         |   0         |   0         |   0         |   0         |      0 |  4976   |   6.8e-08     |  234082           |         228.596   |
| 50%   |   1.78214e+07 |   1.78215e+07 |    72     |      71.5   | 262144           |   3.88173e+11 |     3 |   0         |   0         |   0         |   0         |   0         |      0 | 29636   |   7.2e-08     |       3.47222e+06 |        3390.84    |
| 75%   |   1.84594e+07 |   1.84595e+07 |   152.75  |     134.5   | 262144           |   4.15832e+11 |     3 |   0         |   0         |   0         |   0         |   0         |      0 | 29636   |   1.5275e-07  |       3.67647e+06 |        3590.3     |
| max   |   8.28619e+07 |   8.28621e+07 |  7846     |    7846     |      1.04858e+06 |   4.15882e+11 |     3 |   7         |   6         |   7         |   4         |   9         |      0 | 29636   |   7.846e-06   |       5e+06       |        4882.81    |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |        IBCA |        IACB |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|--------------:|------:|------------:|------------:|------------:|------------:|------------:|--------------:|------------------:|------------------:|
| count |   774     |     774     |    774           | 774           |   774 | 774         | 774         | 774         | 774         | 774         | 774           |     774           |         774       |
| mean  |   259.172 |     236.764 | 203666           |   3.29695e+11 |     3 |   0.0413437 |   0.0439276 |   0.0284238 |   0.0129199 |   0.0335917 |   2.59172e-07 |       2.55077e+06 |        2490.98    |
| std   |   903.308 |     825.96  | 105024           |   1.1777e+11  |     0 |   0.353649  |   0.345936  |   0.303866  |   0.168206  |   0.430299  |   9.03308e-07 |       1.53451e+06 |        1498.54    |
| min   |    11     |       0     |   1024           |   2.70521e+09 |     3 |   0         |   0         |   0         |   0         |   0         |   1.1e-08     |     530.524       |           0.51809 |
| 25%   |    68     |      68     |  65536           |   1.9018e+11  |     3 |   0         |   0         |   0         |   0         |   0         |   6.8e-08     |  234082           |         228.596   |
| 50%   |    72     |      71.5   | 262144           |   3.88173e+11 |     3 |   0         |   0         |   0         |   0         |   0         |   7.2e-08     |       3.47222e+06 |        3390.84    |
| 75%   |   152.75  |     134.5   | 262144           |   4.15832e+11 |     3 |   0         |   0         |   0         |   0         |   0         |   1.5275e-07  |       3.67647e+06 |        3590.3     |
| max   |  7846     |    7846     |      1.04858e+06 |   4.15882e+11 |     3 |   7         |   6         |   7         |   4         |   9         |   7.846e-06   |       5e+06       |        4882.81    |

### IOPS and Throughput Calculations

Total duration of the session: 0.07 seconds

IOPS per disk
|   Disk |     0 |
|-------:|------:|
|      0 | 10381 |

IOPS per IO type
| IO Type   |       0 |
|:----------|--------:|
| Diskread  | 2722.65 |
| Diskwrite | 7658.3  |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       2.55077e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  188127           |
| Diskwrite |       3.39072e+06 |

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
Log-Normal Fit Parameters for IO Time: (0, 0, 4)

### Categorical Features Distribution

#### Value Counts for Categorical Features

Value Counts for IO Type:
| IO Type   |   count |
|:----------|--------:|
| Diskwrite |     571 |
| Diskread  |     203 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |     774 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

