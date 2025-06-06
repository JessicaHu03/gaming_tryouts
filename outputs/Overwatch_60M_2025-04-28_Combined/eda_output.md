# Starting EDA for Overwatch 60M 2025-04-28 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 31401 entries, 0 to 31400
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              31401 non-null  object 
    1   Start Time           31401 non-null  int64  
    2   End Time             31401 non-null  int64  
    3   IO Time              31401 non-null  int64  
    4   Disk SrvT            31401 non-null  int64  
    5   IO Size              31401 non-null  int64  
    6   Byte Offset          31401 non-null  int64  
    7   Pri                  31401 non-null  int64  
    8   QD/I                 31401 non-null  int64  
    9   QD/C                 31401 non-null  int64  
    10  IBCB                 31401 non-null  int64  
    11  IBCA                 31401 non-null  int64  
    12  IACB                 31401 non-null  int64  
    13  Process Name ( PID)  31401 non-null  object 
    14  Disk                 31401 non-null  int64  
    15  Filename             31401 non-null  object 
    16  Process Name         31401 non-null  object 
    17  PID                  31401 non-null  int64  
    18  Duration_s           31401 non-null  float64
    19  Throughput_MB_s      31401 non-null  float64
    20  Throughput_GB_s      31401 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 5.0+ MB
   

## Processed Data Description
|       |      Start Time |        End Time |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |         IBCA |         IACB |   Disk |      PID |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------------:|----------------:|----------:|------------:|-----------------:|----------------:|------:|------------:|------------:|------------:|-------------:|-------------:|-------:|---------:|----------------:|------------------:|------------------:|
| count | 31401           | 31401           | 31401     |   31401     |  31401           | 31401           | 31401 | 31401       | 31401       | 31401       | 31401        | 31401        |  31401 | 31401    | 31401           |   31401           |     31401         |
| mean  |     5.16098e+08 |     5.16099e+08 |   804.411 |     281.049 | 116007           |     1.49382e+11 |     3 |     2.09108 |     2.08968 |     1.67297 |     0.418108 |     0.478074 |      0 |  1556.04 |     8.04411e-07 |  829195           |       809.761     |
| std   |     6.96014e+08 |     6.96014e+08 |  2104.38  |    1251.3   | 271413           |     7.46192e+10 |     0 |     3.6779  |     3.69051 |     3.11639 |     1.38791  |     1.66946  |      0 |  2731.56 |     2.10438e-06 |  878685           |       858.091     |
| min   |     5.48392e+06 |     5.48414e+06 |    10     |       0     |    512           |     2.202e+09   |     3 |     0       |     0       |     0       |    -1        |     0        |      0 |     4    |     1e-08       |      50.385       |         0.0492041 |
| 25%   |     1.96219e+07 |     1.96219e+07 |    54     |      18     |  65536           |     1.06029e+11 |     3 |     0       |     0       |     0       |     0        |     0        |      0 |     4    |     5.4e-08     |  237643           |       232.073     |
| 50%   |     1.52529e+08 |     1.52529e+08 |   125     |      36     |  65536           |     1.24484e+11 |     3 |     1       |     1       |     0       |     0        |     0        |      0 |     4    |     1.25e-07    |  488281           |       476.837     |
| 75%   |     8.00367e+08 |     8.00367e+08 |   251     |      90     |  65536           |     1.66389e+11 |     3 |     3       |     3       |     2       |     0        |     0        |      0 |  4976    |     2.51e-07    |       1.27551e+06 |      1245.62      |
| max   |     2.62584e+09 |     2.62584e+09 | 19656     |   13677     |      2.09715e+06 |     3.53692e+11 |     3 |    63       |    63       |    63       |    33        |    40        |      0 | 20108    |     1.9656e-05  |       5.84795e+06 |      5710.89      |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |         IBCA |         IACB |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|----------------:|------:|------------:|------------:|------------:|-------------:|-------------:|----------------:|------------------:|------------------:|
| count | 31401     |   31401     |  31401           | 31401           | 31401 | 31401       | 31401       | 31401       | 31401        | 31401        | 31401           |   31401           |     31401         |
| mean  |   804.411 |     281.049 | 116007           |     1.49382e+11 |     3 |     2.09108 |     2.08968 |     1.67297 |     0.418108 |     0.478074 |     8.04411e-07 |  829195           |       809.761     |
| std   |  2104.38  |    1251.3   | 271413           |     7.46192e+10 |     0 |     3.6779  |     3.69051 |     3.11639 |     1.38791  |     1.66946  |     2.10438e-06 |  878685           |       858.091     |
| min   |    10     |       0     |    512           |     2.202e+09   |     3 |     0       |     0       |     0       |    -1        |     0        |     1e-08       |      50.385       |         0.0492041 |
| 25%   |    54     |      18     |  65536           |     1.06029e+11 |     3 |     0       |     0       |     0       |     0        |     0        |     5.4e-08     |  237643           |       232.073     |
| 50%   |   125     |      36     |  65536           |     1.24484e+11 |     3 |     1       |     1       |     0       |     0        |     0        |     1.25e-07    |  488281           |       476.837     |
| 75%   |   251     |      90     |  65536           |     1.66389e+11 |     3 |     3       |     3       |     2       |     0        |     0        |     2.51e-07    |       1.27551e+06 |      1245.62      |
| max   | 19656     |   13677     |      2.09715e+06 |     3.53692e+11 |     3 |    63       |    63       |    63       |    33        |    40        |     1.9656e-05  |       5.84795e+06 |      5710.89      |

### IOPS and Throughput Calculations

Total duration of the session: 2.62 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 11983.5 |

IOPS per IO type
| IO Type   |         0 |
|:----------|----------:|
| Diskread  | 11941.5   |
| Diskwrite |    41.979 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |            829195 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |            830454 |
| Diskwrite |            471019 |

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
| Diskread  |   31291 |
| Diskwrite |     110 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |   31401 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

