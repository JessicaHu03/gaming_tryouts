# Starting EDA for Deadlock 60M 2025-05-04 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 924 entries, 0 to 923
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              924 non-null    object 
    1   Start Time           924 non-null    int64  
    2   End Time             924 non-null    int64  
    3   IO Time              924 non-null    int64  
    4   Disk SrvT            924 non-null    int64  
    5   IO Size              924 non-null    int64  
    6   Byte Offset          924 non-null    int64  
    7   Pri                  924 non-null    int64  
    8   QD/I                 924 non-null    int64  
    9   QD/C                 924 non-null    int64  
    10  IBCB                 924 non-null    int64  
    11  IBCA                 924 non-null    int64  
    12  IACB                 924 non-null    int64  
    13  Process Name ( PID)  924 non-null    object 
    14  Disk                 924 non-null    int64  
    15  Filename             924 non-null    object 
    16  Process Name         924 non-null    object 
    17  PID                  924 non-null    int64  
    18  Duration_s           924 non-null    float64
    19  Throughput_MB_s      924 non-null    float64
    20  Throughput_GB_s      924 non-null    float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 151.7+ KB
   

## Processed Data Description
|       |    Start Time |      End Time |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |       QD/I |       QD/C |       IBCB |       IBCA |        IACB |   Disk |     PID |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|--------------:|--------------:|----------:|------------:|-----------------:|--------------:|------:|-----------:|-----------:|-----------:|-----------:|------------:|-------:|--------:|--------------:|------------------:|------------------:|
| count | 924           | 924           |    924    |      924    |    924           | 924           |   924 | 924        | 924        | 924        | 924        | 924         |    924 |   924   | 924           |     924           |        924        |
| mean  |   3.55831e+08 |   3.55832e+08 |   1416.55 |     1044.9  | 317747           |   1.67363e+11 |     3 |   0.169913 |   0.152597 |   0.130952 |   0.038961 |   0.0638528 |      0 | 29519.2 |   1.41655e-06 |       2.2243e+06  |       2172.17     |
| std   |   8.575e+08   |   8.57501e+08 |   3796.41 |     3302.48 | 402055           |   5.68645e+10 |     0 |   0.601842 |   0.575298 |   0.523712 |   0.229459 |   0.391171  |      0 | 15776.8 |   3.79641e-06 |       1.616e+06   |       1578.12     |
| min   |   5.29486e+06 |   5.29487e+06 |     10    |        0    |   1024           |   2.43233e+09 |     3 |   0        |   0        |   0        |   0        |   0         |      0 |     4   |   1e-08       |     127.057       |          0.124079 |
| 25%   |   1.91569e+07 |   1.9157e+07  |     68    |       68    |  65536           |   1.74925e+11 |     3 |   0        |   0        |   0        |   0        |   0         |      0 |  4976   |   6.8e-08     |  210971           |        206.026    |
| 50%   |   1.95195e+07 |   1.95195e+07 |     72    |       72    | 262144           |   1.91573e+11 |     3 |   0        |   0        |   0        |   0        |   0         |      0 | 39152   |   7.2e-08     |       3.3114e+06  |       3233.79     |
| 75%   |   3.05699e+07 |   3.05702e+07 |    309    |      285.25 | 262144           |   1.93696e+11 |     3 |   0        |   0        |   0        |   0        |   0         |      0 | 39152   |   3.09e-07    |       3.67647e+06 |       3590.3      |
| max   |   3.82878e+09 |   3.82878e+09 |  28573    |    28416    |      2.09715e+06 |   2.58519e+11 |     3 |   5        |   5        |   5        |   2        |   5         |      0 | 39152   |   2.8573e-05  |       4.54545e+06 |       4438.92     |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |   Byte Offset |   Pri |       QD/I |       QD/C |       IBCB |       IBCA |        IACB |    Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|--------------:|------:|-----------:|-----------:|-----------:|-----------:|------------:|--------------:|------------------:|------------------:|
| count |    924    |      924    |    924           | 924           |   924 | 924        | 924        | 924        | 924        | 924         | 924           |     924           |        924        |
| mean  |   1416.55 |     1044.9  | 317747           |   1.67363e+11 |     3 |   0.169913 |   0.152597 |   0.130952 |   0.038961 |   0.0638528 |   1.41655e-06 |       2.2243e+06  |       2172.17     |
| std   |   3796.41 |     3302.48 | 402055           |   5.68645e+10 |     0 |   0.601842 |   0.575298 |   0.523712 |   0.229459 |   0.391171  |   3.79641e-06 |       1.616e+06   |       1578.12     |
| min   |     10    |        0    |   1024           |   2.43233e+09 |     3 |   0        |   0        |   0        |   0        |   0         |   1e-08       |     127.057       |          0.124079 |
| 25%   |     68    |       68    |  65536           |   1.74925e+11 |     3 |   0        |   0        |   0        |   0        |   0         |   6.8e-08     |  210971           |        206.026    |
| 50%   |     72    |       72    | 262144           |   1.91573e+11 |     3 |   0        |   0        |   0        |   0        |   0         |   7.2e-08     |       3.3114e+06  |       3233.79     |
| 75%   |    309    |      285.25 | 262144           |   1.93696e+11 |     3 |   0        |   0        |   0        |   0        |   0         |   3.09e-07    |       3.67647e+06 |       3590.3      |
| max   |  28573    |    28416    |      2.09715e+06 |   2.58519e+11 |     3 |   5        |   5        |   5        |   2        |   5         |   2.8573e-05  |       4.54545e+06 |       4438.92     |

### IOPS and Throughput Calculations

Total duration of the session: 3.82 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 241.664 |

IOPS per IO type
| IO Type   |        0 |
|:----------|---------:|
| Diskread  |  81.3394 |
| Diskwrite | 160.325  |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |        2.2243e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  330471           |
| Diskwrite |       3.18511e+06 |

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
| Diskwrite |     613 |
| Diskread  |     311 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |     924 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

