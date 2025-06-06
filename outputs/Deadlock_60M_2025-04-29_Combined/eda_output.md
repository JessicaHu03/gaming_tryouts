# Starting EDA for Deadlock 60M 2025-04-29 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 14345 entries, 0 to 14344
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              14345 non-null  object 
    1   Start Time           14345 non-null  int64  
    2   End Time             14345 non-null  int64  
    3   IO Time              14345 non-null  int64  
    4   Disk SrvT            14345 non-null  int64  
    5   IO Size              14345 non-null  int64  
    6   Byte Offset          14345 non-null  int64  
    7   Pri                  14345 non-null  int64  
    8   QD/I                 14345 non-null  int64  
    9   QD/C                 14345 non-null  int64  
    10  IBCB                 14345 non-null  int64  
    11  IBCA                 14345 non-null  int64  
    12  IACB                 14345 non-null  int64  
    13  Process Name ( PID)  14345 non-null  object 
    14  Disk                 14345 non-null  int64  
    15  Filename             14345 non-null  object 
    16  Process Name         14345 non-null  object 
    17  PID                  14345 non-null  int64  
    18  Duration_s           14345 non-null  float64
    19  Throughput_MB_s      14345 non-null  float64
    20  Throughput_GB_s      14345 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 2.3+ MB
   

## Processed Data Description
|       |      Start Time |        End Time |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |         QD/I |         QD/C |        IBCB |         IBCA |         IACB |   Disk |      PID |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------------:|----------------:|----------:|------------:|-----------------:|----------------:|------:|-------------:|-------------:|------------:|-------------:|-------------:|-------:|---------:|----------------:|------------------:|------------------:|
| count | 14345           | 14345           |  14345    |   14345     |  14345           | 14345           | 14345 | 14345        | 14345        | 14345       | 14345        | 14345        |  14345 | 14345    | 14345           |   14345           |     14345         |
| mean  |     2.48071e+08 |     2.48073e+08 |   1400.92 |     742.418 | 768149           |     1.75432e+11 |     3 |     0.915162 |     0.919484 |     0.78794 |     0.127222 |     0.177065 |      0 | 28577.4  |     1.40092e-06 |       1.58882e+06 |      1551.58      |
| std   |     5.63695e+08 |     5.63696e+08 |   2751.1  |    2062.49  | 666812           |     9.04135e+10 |     0 |     3.48721  |     3.51735  |     3.3725  |     0.497822 |     0.903927 |      0 |  8031.13 |     2.7511e-06  |       1.30829e+06 |      1277.63      |
| min   |     4.26212e+06 |     4.26214e+06 |      9    |       0     |    512           |     2.1323e+09  |     3 |     0        |     0        |     0       |    -3        |     0        |      0 |     4    |     9e-09       |      63.167       |         0.0616866 |
| 25%   |     1.84778e+07 |     1.84778e+07 |     87    |      68     |  65536           |     1.69218e+11 |     3 |     0        |     0        |     0       |     0        |     0        |      0 | 31764    |     8.7e-08     |  431142           |       421.037     |
| 50%   |     3.32675e+07 |     3.32686e+07 |    468    |     167     |      1.04858e+06 |     1.8184e+11  |     3 |     0        |     0        |     0       |     0        |     0        |      0 | 31764    |     4.68e-07    |       1.35685e+06 |      1325.05      |
| 75%   |     1.17614e+08 |     1.17615e+08 |    899    |     495     |      1.04858e+06 |     1.92336e+11 |     3 |     1        |     1        |     0       |     0        |     0        |      0 | 31764    |     8.99e-07    |       2.40385e+06 |      2347.51      |
| max   |     4.15516e+09 |     4.15516e+09 |  35382    |   35382     |      2.09715e+06 |     3.53767e+11 |     3 |    61        |    61        |    61       |     8        |    35        |      0 | 32164    |     3.5382e-05  |       5.89767e+06 |      5759.44      |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |         QD/I |         QD/C |        IBCB |         IBCA |         IACB |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|----------------:|------:|-------------:|-------------:|------------:|-------------:|-------------:|----------------:|------------------:|------------------:|
| count |  14345    |   14345     |  14345           | 14345           | 14345 | 14345        | 14345        | 14345       | 14345        | 14345        | 14345           |   14345           |     14345         |
| mean  |   1400.92 |     742.418 | 768149           |     1.75432e+11 |     3 |     0.915162 |     0.919484 |     0.78794 |     0.127222 |     0.177065 |     1.40092e-06 |       1.58882e+06 |      1551.58      |
| std   |   2751.1  |    2062.49  | 666812           |     9.04135e+10 |     0 |     3.48721  |     3.51735  |     3.3725  |     0.497822 |     0.903927 |     2.7511e-06  |       1.30829e+06 |      1277.63      |
| min   |      9    |       0     |    512           |     2.1323e+09  |     3 |     0        |     0        |     0       |    -3        |     0        |     9e-09       |      63.167       |         0.0616866 |
| 25%   |     87    |      68     |  65536           |     1.69218e+11 |     3 |     0        |     0        |     0       |     0        |     0        |     8.7e-08     |  431142           |       421.037     |
| 50%   |    468    |     167     |      1.04858e+06 |     1.8184e+11  |     3 |     0        |     0        |     0       |     0        |     0        |     4.68e-07    |       1.35685e+06 |      1325.05      |
| 75%   |    899    |     495     |      1.04858e+06 |     1.92336e+11 |     3 |     1        |     1        |     0       |     0        |     0        |     8.99e-07    |       2.40385e+06 |      2347.51      |
| max   |  35382    |   35382     |      2.09715e+06 |     3.53767e+11 |     3 |    61        |    61        |    61       |     8        |    35        |     3.5382e-05  |       5.89767e+06 |      5759.44      |

### IOPS and Throughput Calculations

Total duration of the session: 4.15 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 3455.88 |

IOPS per IO type
| IO Type   |        0 |
|:----------|---------:|
| Diskread  | 3002.97  |
| Diskwrite |  452.915 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.58882e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.35244e+06 |
| Diskwrite |       3.1561e+06  |

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
Log-Normal Fit Parameters for IO Time: (0, 0, 5)

### Categorical Features Distribution

#### Value Counts for Categorical Features

Value Counts for IO Type:
| IO Type   |   count |
|:----------|--------:|
| Diskread  |   12465 |
| Diskwrite |    1880 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |   14345 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

