# Starting EDA for Deadlock 60M 2025-04-28 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 11682 entries, 0 to 11681
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              11682 non-null  object 
    1   Start Time           11682 non-null  int64  
    2   End Time             11682 non-null  int64  
    3   IO Time              11682 non-null  int64  
    4   Disk SrvT            11682 non-null  int64  
    5   IO Size              11682 non-null  int64  
    6   Byte Offset          11682 non-null  int64  
    7   Pri                  11682 non-null  int64  
    8   QD/I                 11682 non-null  int64  
    9   QD/C                 11682 non-null  int64  
    10  IBCB                 11682 non-null  int64  
    11  IBCA                 11682 non-null  int64  
    12  IACB                 11682 non-null  int64  
    13  Process Name ( PID)  11682 non-null  object 
    14  Disk                 11682 non-null  int64  
    15  Filename             11682 non-null  object 
    16  Process Name         11682 non-null  object 
    17  PID                  11682 non-null  int64  
    18  Duration_s           11682 non-null  float64
    19  Throughput_MB_s      11682 non-null  float64
    20  Throughput_GB_s      11682 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 1.9+ MB
   

## Processed Data Description
|       |      Start Time |        End Time |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |         IBCA |         IACB |   Disk |      PID |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------------:|----------------:|----------:|------------:|-----------------:|----------------:|------:|------------:|------------:|------------:|-------------:|-------------:|-------:|---------:|----------------:|------------------:|------------------:|
| count | 11682           | 11682           |  11682    |   11682     |  11682           | 11682           | 11682 | 11682       | 11682       | 11682       | 11682        | 11682        |  11682 | 11682    | 11682           |   11682           |     11682         |
| mean  |     3.0357e+08  |     3.03571e+08 |   1305.9  |     614.871 | 879875           |     1.70645e+11 |     3 |     1.25458 |     1.264   |     1.05684 |     0.19774  |     0.220681 |      0 | 22788.6  |     1.3059e-06  |       1.80453e+06 |      1762.23      |
| std   |     5.46891e+08 |     5.46892e+08 |   2826.26 |    2100.91  | 665340           |     8.62745e+10 |     0 |     3.92613 |     3.94392 |     3.73378 |     0.750494 |     0.834733 |      0 |  5968.36 |     2.82626e-06 |       1.30634e+06 |      1275.72      |
| min   |     8.36196e+06 |     8.36198e+06 |      9    |       0     |    512           |     2.10892e+09 |     3 |     0       |     0       |     0       |    -1        |     0        |      0 |     4    |     9e-09       |      48.0166      |         0.0468913 |
| 25%   |     7.25176e+07 |     7.25258e+07 |    161.25 |      71     | 262144           |     1.69364e+11 |     3 |     0       |     0       |     0       |     0        |     0        |      0 | 24000    |     1.6125e-07  |  572092           |       558.684     |
| 50%   |     9.13707e+07 |     9.13712e+07 |    468    |     197     |      1.04858e+06 |     1.81528e+11 |     3 |     0       |     0       |     0       |     0        |     0        |      0 | 24000    |     4.68e-07    |       1.75411e+06 |      1712.99      |
| 75%   |     2.18003e+08 |     2.18004e+08 |    770.75 |     430.75  |      1.04858e+06 |     1.90802e+11 |     3 |     1       |     1       |     1       |     0        |     0        |      0 | 24000    |     7.7075e-07  |       2.60417e+06 |      2543.13      |
| max   |     3.21113e+09 |     3.21113e+09 |  35421    |   35340     |      2.09715e+06 |     3.50748e+11 |     3 |    55       |    55       |    54       |    13        |    14        |      0 | 29416    |     3.5421e-05  |       5.88235e+06 |      5744.49      |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |         IBCA |         IACB |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|----------------:|------:|------------:|------------:|------------:|-------------:|-------------:|----------------:|------------------:|------------------:|
| count |  11682    |   11682     |  11682           | 11682           | 11682 | 11682       | 11682       | 11682       | 11682        | 11682        | 11682           |   11682           |     11682         |
| mean  |   1305.9  |     614.871 | 879875           |     1.70645e+11 |     3 |     1.25458 |     1.264   |     1.05684 |     0.19774  |     0.220681 |     1.3059e-06  |       1.80453e+06 |      1762.23      |
| std   |   2826.26 |    2100.91  | 665340           |     8.62745e+10 |     0 |     3.92613 |     3.94392 |     3.73378 |     0.750494 |     0.834733 |     2.82626e-06 |       1.30634e+06 |      1275.72      |
| min   |      9    |       0     |    512           |     2.10892e+09 |     3 |     0       |     0       |     0       |    -1        |     0        |     9e-09       |      48.0166      |         0.0468913 |
| 25%   |    161.25 |      71     | 262144           |     1.69364e+11 |     3 |     0       |     0       |     0       |     0        |     0        |     1.6125e-07  |  572092           |       558.684     |
| 50%   |    468    |     197     |      1.04858e+06 |     1.81528e+11 |     3 |     0       |     0       |     0       |     0        |     0        |     4.68e-07    |       1.75411e+06 |      1712.99      |
| 75%   |    770.75 |     430.75  |      1.04858e+06 |     1.90802e+11 |     3 |     1       |     1       |     1       |     0        |     0        |     7.7075e-07  |       2.60417e+06 |      2543.13      |
| max   |  35421    |   35340     |      2.09715e+06 |     3.50748e+11 |     3 |    55       |    55       |    54       |    13        |    14        |     3.5421e-05  |       5.88235e+06 |      5744.49      |

### IOPS and Throughput Calculations

Total duration of the session: 3.20 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 3647.47 |

IOPS per IO type
| IO Type   |        0 |
|:----------|---------:|
| Diskread  | 3261.86  |
| Diskwrite |  385.604 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.80453e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.63674e+06 |
| Diskwrite |       3.22383e+06 |

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
| Diskread  |   10447 |
| Diskwrite |    1235 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |   11682 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

