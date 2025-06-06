# Starting EDA for Deadlock 60M 2025-05-03 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 2107 entries, 0 to 2106
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              2107 non-null   object 
    1   Start Time           2107 non-null   int64  
    2   End Time             2107 non-null   int64  
    3   IO Time              2107 non-null   int64  
    4   Disk SrvT            2107 non-null   int64  
    5   IO Size              2107 non-null   int64  
    6   Byte Offset          2107 non-null   int64  
    7   Pri                  2107 non-null   int64  
    8   QD/I                 2107 non-null   int64  
    9   QD/C                 2107 non-null   int64  
    10  IBCB                 2107 non-null   int64  
    11  IBCA                 2107 non-null   int64  
    12  IACB                 2107 non-null   int64  
    13  Process Name ( PID)  2107 non-null   object 
    14  Disk                 2107 non-null   int64  
    15  Filename             2107 non-null   object 
    16  Process Name         2107 non-null   object 
    17  PID                  2107 non-null   int64  
    18  Duration_s           2107 non-null   float64
    19  Throughput_MB_s      2107 non-null   float64
    20  Throughput_GB_s      2107 non-null   float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 345.8+ KB
   

## Processed Data Description
|       |     Start Time |       End Time |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |         QD/I |         QD/C |        IBCB |         IBCA |         IACB |   Disk |     PID |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|---------------:|---------------:|----------:|------------:|-----------------:|---------------:|------:|-------------:|-------------:|------------:|-------------:|-------------:|-------:|--------:|---------------:|------------------:|------------------:|
| count | 2107           | 2107           |  2107     |    2107     |   2107           | 2107           |  2107 | 2107         | 2107         | 2107        | 2107         | 2107         |   2107 |  2107   | 2107           |    2107           |       2107        |
| mean  |    6.25486e+08 |    6.25487e+08 |   517.075 |     433.516 | 256364           |    1.87726e+11 |     3 |    0.0987186 |    0.0915994 |    0.078785 |    0.0199336 |    0.0175605 |      0 | 21848.6 |    5.17075e-07 |       2.84976e+06 |       2782.97     |
| std   |    9.41219e+08 |    9.41219e+08 |  2104.1   |    1956.98  | 239805           |    5.18804e+10 |     0 |    0.639573  |    0.614529  |    0.571947 |    0.170418  |    0.200131  |      0 | 11687.7 |    2.1041e-06  |       1.39653e+06 |       1363.8      |
| min   |    1.8277e+06  |    1.82793e+06 |    11     |       0     |   1024           |    2.43233e+09 |     3 |    0         |    0         |    0        |    0         |    0         |      0 |     4   |    1.1e-08     |     127.873       |          0.124876 |
| 25%   |    1.7064e+07  |    1.70641e+07 |    67     |      67     | 262144           |    1.93645e+11 |     3 |    0         |    0         |    0        |    0         |    0         |      0 | 13900   |    6.7e-08     |       2.80899e+06 |       2743.15     |
| 50%   |    1.7429e+07  |    1.74291e+07 |    69     |      69     | 262144           |    2.07954e+11 |     3 |    0         |    0         |    0        |    0         |    0         |      0 | 27272   |    6.9e-08     |       3.57143e+06 |       3487.72     |
| 75%   |    2.13247e+09 |    2.13247e+09 |    77     |      76     | 262144           |    2.09305e+11 |     3 |    0         |    0         |    0        |    0         |    0         |      0 | 36220   |    7.7e-08     |       3.73134e+06 |       3643.89     |
| max   |    2.13371e+09 |    2.13371e+09 | 28076     |   28076     |      2.09715e+06 |    3.3288e+11  |     3 |    9         |    9         |    9        |    4         |    4         |      0 | 36220   |    2.8076e-05  |       5.20833e+06 |       5086.26     |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |         QD/I |         QD/C |        IBCB |         IBCA |         IACB |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|---------------:|------:|-------------:|-------------:|------------:|-------------:|-------------:|---------------:|------------------:|------------------:|
| count |  2107     |    2107     |   2107           | 2107           |  2107 | 2107         | 2107         | 2107        | 2107         | 2107         | 2107           |    2107           |       2107        |
| mean  |   517.075 |     433.516 | 256364           |    1.87726e+11 |     3 |    0.0987186 |    0.0915994 |    0.078785 |    0.0199336 |    0.0175605 |    5.17075e-07 |       2.84976e+06 |       2782.97     |
| std   |  2104.1   |    1956.98  | 239805           |    5.18804e+10 |     0 |    0.639573  |    0.614529  |    0.571947 |    0.170418  |    0.200131  |    2.1041e-06  |       1.39653e+06 |       1363.8      |
| min   |    11     |       0     |   1024           |    2.43233e+09 |     3 |    0         |    0         |    0        |    0         |    0         |    1.1e-08     |     127.873       |          0.124876 |
| 25%   |    67     |      67     | 262144           |    1.93645e+11 |     3 |    0         |    0         |    0        |    0         |    0         |    6.7e-08     |       2.80899e+06 |       2743.15     |
| 50%   |    69     |      69     | 262144           |    2.07954e+11 |     3 |    0         |    0         |    0        |    0         |    0         |    6.9e-08     |       3.57143e+06 |       3487.72     |
| 75%   |    77     |      76     | 262144           |    2.09305e+11 |     3 |    0         |    0         |    0        |    0         |    0         |    7.7e-08     |       3.73134e+06 |       3643.89     |
| max   | 28076     |   28076     |      2.09715e+06 |    3.3288e+11  |     3 |    9         |    9         |    9        |    4         |    4         |    2.8076e-05  |       5.20833e+06 |       5086.26     |

### IOPS and Throughput Calculations

Total duration of the session: 2.13 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 988.328 |

IOPS per IO type
| IO Type   |       0 |
|:----------|--------:|
| Diskread  | 174.494 |
| Diskwrite | 813.835 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       2.84976e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  242318           |
| Diskwrite |       3.40882e+06 |

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
| Diskwrite |    1735 |
| Diskread  |     372 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |    2107 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

