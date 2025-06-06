# Starting EDA for Marvel Rivals 60M 2025-05-06 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 71509 entries, 0 to 71508
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              71509 non-null  object 
    1   Start Time           71509 non-null  int64  
    2   End Time             71509 non-null  int64  
    3   IO Time              71509 non-null  int64  
    4   Disk SrvT            71509 non-null  int64  
    5   IO Size              71509 non-null  int64  
    6   Byte Offset          71509 non-null  int64  
    7   Pri                  71509 non-null  int64  
    8   QD/I                 71509 non-null  int64  
    9   QD/C                 71509 non-null  int64  
    10  IBCB                 71509 non-null  int64  
    11  IBCA                 71509 non-null  int64  
    12  IACB                 71509 non-null  int64  
    13  Process Name ( PID)  71509 non-null  object 
    14  Disk                 71509 non-null  int64  
    15  Filename             71509 non-null  object 
    16  Process Name         71509 non-null  object 
    17  PID                  71509 non-null  int64  
    18  Duration_s           71509 non-null  float64
    19  Throughput_MB_s      71509 non-null  float64
    20  Throughput_GB_s      71509 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 11.5+ MB
   

## Processed Data Description
|       |      Start Time |        End Time |    IO Time |   Disk SrvT |          IO Size |     Byte Offset |           Pri |        QD/I |         QD/C |         IBCB |          IBCA |          IACB |   Disk |     PID |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------------:|----------------:|-----------:|------------:|-----------------:|----------------:|--------------:|------------:|-------------:|-------------:|--------------:|--------------:|-------:|--------:|----------------:|------------------:|------------------:|
| count | 71509           | 71509           |  71509     |   71509     |  71509           | 71509           | 71509         | 71509       | 71509        | 71509        | 71509         | 71509         |  71509 | 71509   | 71509           |   71509           |     71509         |
| mean  |     3.92668e+08 |     3.92668e+08 |    338.796 |     267.229 | 161592           |     2.40592e+11 |     2.99986   |     0.3128  |     0.312884 |     0.263142 |     0.0496581 |     0.0625516 |      0 | 11838.9 |     3.38796e-07 |       1.20125e+06 |      1173.1       |
| std   |     3.04049e+08 |     3.04049e+08 |   1552.46  |    1356.8   | 204432           |     1.18294e+11 |     0.0167233 |     2.33426 |     2.33475  |     2.18262  |     0.413535  |     0.669825  |      0 | 18702.9 |     1.55246e-06 |       1.07482e+06 |      1049.63      |
| min   |     2.3521e+06  |     2.35238e+06 |     10     |       0     |    512           |     5.56257e+08 |     1         |     0       |     0        |     0        |    -2         |     0         |      0 |     4   |     1e-08       |      27.2235      |         0.0265855 |
| 25%   |     1.55422e+08 |     1.55422e+08 |     56     |      50     |  36864           |     2.07859e+11 |     3         |     0       |     0        |     0        |     0         |     0         |      0 |     4   |     5.6e-08     |  249335           |       243.491     |
| 50%   |     3.08507e+08 |     3.08507e+08 |     93     |      85     |  65536           |     2.7995e+11  |     3         |     0       |     0        |     0        |     0         |     0         |      0 |     4   |     9.3e-08     |  950863           |       928.578     |
| 75%   |     6.82933e+08 |     6.82933e+08 |    198     |     183     | 262144           |     3.25852e+11 |     3         |     0       |     0        |     0        |     0         |     0         |      0 | 10940   |     1.98e-07    |       1.6572e+06  |      1618.36      |
| max   |     1.17195e+09 |     1.17196e+09 | 245751     |  245751     |      2.09715e+06 |     4.16133e+11 |     3         |    72       |    72        |    72        |    18         |    49         |      0 | 51920   |     0.000245751 |       5.74713e+06 |      5612.43      |

## Description of Selected Columns
|       |    IO Time |   Disk SrvT |          IO Size |     Byte Offset |           Pri |        QD/I |         QD/C |         IBCB |          IBCA |          IACB |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------:|------------:|-----------------:|----------------:|--------------:|------------:|-------------:|-------------:|--------------:|--------------:|----------------:|------------------:|------------------:|
| count |  71509     |   71509     |  71509           | 71509           | 71509         | 71509       | 71509        | 71509        | 71509         | 71509         | 71509           |   71509           |     71509         |
| mean  |    338.796 |     267.229 | 161592           |     2.40592e+11 |     2.99986   |     0.3128  |     0.312884 |     0.263142 |     0.0496581 |     0.0625516 |     3.38796e-07 |       1.20125e+06 |      1173.1       |
| std   |   1552.46  |    1356.8   | 204432           |     1.18294e+11 |     0.0167233 |     2.33426 |     2.33475  |     2.18262  |     0.413535  |     0.669825  |     1.55246e-06 |       1.07482e+06 |      1049.63      |
| min   |     10     |       0     |    512           |     5.56257e+08 |     1         |     0       |     0        |     0        |    -2         |     0         |     1e-08       |      27.2235      |         0.0265855 |
| 25%   |     56     |      50     |  36864           |     2.07859e+11 |     3         |     0       |     0        |     0        |     0         |     0         |     5.6e-08     |  249335           |       243.491     |
| 50%   |     93     |      85     |  65536           |     2.7995e+11  |     3         |     0       |     0        |     0        |     0         |     0         |     9.3e-08     |  950863           |       928.578     |
| 75%   |    198     |     183     | 262144           |     3.25852e+11 |     3         |     0       |     0        |     0        |     0         |     0         |     1.98e-07    |       1.6572e+06  |      1618.36      |
| max   | 245751     |  245751     |      2.09715e+06 |     4.16133e+11 |     3         |    72       |    72        |    72        |    18         |    49         |     0.000245751 |       5.74713e+06 |      5612.43      |

### IOPS and Throughput Calculations

Total duration of the session: 1.17 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 61139.5 |

IOPS per IO type
| IO Type   |        0 |
|:----------|---------:|
| Diskread  | 59309.8  |
| Diskwrite |  1829.68 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.20125e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.21858e+06 |
| Diskwrite |  639383           |

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
| Diskread  |   69369 |
| Diskwrite |    2140 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |   71509 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

