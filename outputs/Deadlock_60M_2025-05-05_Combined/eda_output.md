# Starting EDA for Deadlock 60M 2025-05-05 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 1711 entries, 0 to 1710
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              1711 non-null   object 
    1   Start Time           1711 non-null   int64  
    2   End Time             1711 non-null   int64  
    3   IO Time              1711 non-null   int64  
    4   Disk SrvT            1711 non-null   int64  
    5   IO Size              1711 non-null   int64  
    6   Byte Offset          1711 non-null   int64  
    7   Pri                  1711 non-null   int64  
    8   QD/I                 1711 non-null   int64  
    9   QD/C                 1711 non-null   int64  
    10  IBCB                 1711 non-null   int64  
    11  IBCA                 1711 non-null   int64  
    12  IACB                 1711 non-null   int64  
    13  Process Name ( PID)  1711 non-null   object 
    14  Disk                 1711 non-null   int64  
    15  Filename             1711 non-null   object 
    16  Process Name         1711 non-null   object 
    17  PID                  1711 non-null   int64  
    18  Duration_s           1711 non-null   float64
    19  Throughput_MB_s      1711 non-null   float64
    20  Throughput_GB_s      1711 non-null   float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 280.8+ KB
   

## Processed Data Description
|       |     Start Time |       End Time |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |         QD/I |        QD/C |         IBCB |         IBCA |         IACB |   Disk |     PID |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|---------------:|---------------:|----------:|------------:|-----------------:|---------------:|------:|-------------:|------------:|-------------:|-------------:|-------------:|-------:|--------:|---------------:|------------------:|------------------:|
| count | 1711           | 1711           |   1711    |    1711     |   1711           | 1711           |  1711 | 1711         | 1711        | 1711         | 1711         | 1711         |   1711 |  1711   | 1711           |    1711           |       1711        |
| mean  |    1.33349e+08 |    1.3335e+08  |   1074.22 |     962.434 | 221688           |    1.50363e+11 |     3 |    0.0970193 |    0.111631 |    0.0619521 |    0.0350672 |    0.0280538 |      0 | 34885.1 |    1.07422e-06 |       2.38779e+06 |       2331.83     |
| std   |    4.70162e+08 |    4.70163e+08 |   3538.43 |    3346.07  | 196876           |    7.04912e+10 |     0 |    0.504885  |    0.519603 |    0.338066  |    0.264792  |    0.256669  |      0 | 19390   |    3.53843e-06 |       1.63725e+06 |       1598.88     |
| min   |    2.59839e+06 |    2.5984e+06  |     10    |       0     |   1024           |    2.25853e+09 |     3 |    0         |    0        |    0         |    0         |    0         |      0 |     4   |    1e-08       |     127.09        |          0.124112 |
| 25%   |    1.67901e+07 |    1.67901e+07 |     67    |      67     |  65536           |    8.24414e+10 |     3 |    0         |    0        |    0         |    0         |    0         |      0 |  4976   |    6.7e-08     |  217110           |        212.022    |
| 50%   |    1.73386e+07 |    1.73387e+07 |     70    |      70     | 262144           |    1.80113e+11 |     3 |    0         |    0        |    0         |    0         |    0         |      0 | 46020   |    7e-08       |       3.52113e+06 |       3438.6      |
| 75%   |    2.66265e+07 |    2.66307e+07 |    274.5  |     265     | 262144           |    2.07933e+11 |     3 |    0         |    0        |    0         |    0         |    0         |      0 | 48008   |    2.745e-07   |       3.67647e+06 |       3590.3      |
| max   |    4.01046e+09 |    4.01046e+09 |  35586    |   35586     |      2.09715e+06 |    3.30078e+11 |     3 |    8         |    7        |    5         |    4         |    5         |      0 | 48008   |    3.5586e-05  |       5e+06       |       4882.81     |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |         QD/I |        QD/C |         IBCB |         IBCA |         IACB |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|---------------:|------:|-------------:|------------:|-------------:|-------------:|-------------:|---------------:|------------------:|------------------:|
| count |   1711    |    1711     |   1711           | 1711           |  1711 | 1711         | 1711        | 1711         | 1711         | 1711         | 1711           |    1711           |       1711        |
| mean  |   1074.22 |     962.434 | 221688           |    1.50363e+11 |     3 |    0.0970193 |    0.111631 |    0.0619521 |    0.0350672 |    0.0280538 |    1.07422e-06 |       2.38779e+06 |       2331.83     |
| std   |   3538.43 |    3346.07  | 196876           |    7.04912e+10 |     0 |    0.504885  |    0.519603 |    0.338066  |    0.264792  |    0.256669  |    3.53843e-06 |       1.63725e+06 |       1598.88     |
| min   |     10    |       0     |   1024           |    2.25853e+09 |     3 |    0         |    0        |    0         |    0         |    0         |    1e-08       |     127.09        |          0.124112 |
| 25%   |     67    |      67     |  65536           |    8.24414e+10 |     3 |    0         |    0        |    0         |    0         |    0         |    6.7e-08     |  217110           |        212.022    |
| 50%   |     70    |      70     | 262144           |    1.80113e+11 |     3 |    0         |    0        |    0         |    0         |    0         |    7e-08       |       3.52113e+06 |       3438.6      |
| 75%   |    274.5  |     265     | 262144           |    2.07933e+11 |     3 |    0         |    0        |    0         |    0         |    0         |    2.745e-07   |       3.67647e+06 |       3590.3      |
| max   |  35586    |   35586     |      2.09715e+06 |    3.30078e+11 |     3 |    8         |    7        |    5         |    4         |    5         |    3.5586e-05  |       5e+06       |       4882.81     |

### IOPS and Throughput Calculations

Total duration of the session: 4.01 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 426.911 |

IOPS per IO type
| IO Type   |       0 |
|:----------|--------:|
| Diskread  | 124.505 |
| Diskwrite | 302.405 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       2.38779e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  185691           |
| Diskwrite |       3.29444e+06 |

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
| Diskwrite |    1212 |
| Diskread  |     499 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |    1711 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

