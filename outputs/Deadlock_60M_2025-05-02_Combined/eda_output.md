# Starting EDA for Deadlock 60M 2025-05-02 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 1211 entries, 0 to 1210
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              1211 non-null   object 
    1   Start Time           1211 non-null   int64  
    2   End Time             1211 non-null   int64  
    3   IO Time              1211 non-null   int64  
    4   Disk SrvT            1211 non-null   int64  
    5   IO Size              1211 non-null   int64  
    6   Byte Offset          1211 non-null   int64  
    7   Pri                  1211 non-null   int64  
    8   QD/I                 1211 non-null   int64  
    9   QD/C                 1211 non-null   int64  
    10  IBCB                 1211 non-null   int64  
    11  IBCA                 1211 non-null   int64  
    12  IACB                 1211 non-null   int64  
    13  Process Name ( PID)  1211 non-null   object 
    14  Disk                 1211 non-null   int64  
    15  Filename             1211 non-null   object 
    16  Process Name         1211 non-null   object 
    17  PID                  1211 non-null   int64  
    18  Duration_s           1211 non-null   float64
    19  Throughput_MB_s      1211 non-null   float64
    20  Throughput_GB_s      1211 non-null   float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 198.8+ KB
   

## Processed Data Description
|       |     Start Time |       End Time |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |        IBCA |        IACB |   Disk |      PID |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|---------------:|---------------:|----------:|------------:|-----------------:|---------------:|------:|------------:|------------:|------------:|------------:|------------:|-------:|---------:|---------------:|------------------:|------------------:|
| count | 1211           | 1211           |   1211    |     1211    |   1211           | 1211           |  1211 | 1211        | 1211        | 1211        | 1211        | 1211        |   1211 |  1211    | 1211           |    1211           |       1211        |
| mean  |    3.91214e+08 |    3.91216e+08 |   2008.28 |     1355.45 | 582567           |    2.14382e+11 |     3 |    0.391412 |    0.388935 |    0.212221 |    0.179191 |    0.109827 |      0 | 30364.7  |    2.00828e-06 |       2.04088e+06 |       1993.05     |
| std   |    7.37257e+08 |    7.37259e+08 |   4708.74 |     3749.07 | 583555           |    9.75922e+10 |     0 |    0.854966 |    0.834094 |    0.669562 |    0.501333 |    0.406957 |      0 |  8714.83 |    4.70874e-06 |       1.48961e+06 |       1454.7      |
| min   |    3.95052e+07 |    3.95052e+07 |     10    |        0    |   1536           |    5.57879e+08 |     3 |    0        |    0        |    0        |   -1        |    0        |      0 |     4    |    1e-08       |     197.047       |          0.192428 |
| 25%   |    5.37977e+07 |    5.37978e+07 |     69    |       68    | 262144           |    1.75703e+11 |     3 |    0        |    0        |    0        |    0        |    0        |      0 | 33012    |    6.9e-08     |  348192           |        340.031    |
| 50%   |    9.1874e+07  |    9.18746e+07 |    123    |       78    | 262144           |    2.55313e+11 |     3 |    0        |    0        |    0        |    0        |    0        |      0 | 33012    |    1.23e-07    |       2.079e+06   |       2030.28     |
| 75%   |    3.71936e+08 |    3.71937e+08 |    898.5  |      533.5  |      1.04858e+06 |    2.57406e+11 |     3 |    1        |    1        |    0        |    0        |    0        |      0 | 33012    |    8.985e-07   |       3.57143e+06 |       3487.72     |
| max   |    4.01657e+09 |    4.01657e+09 |  29899    |    28323    |      2.09715e+06 |    3.75918e+11 |     3 |    7        |    7        |    7        |    5        |    4        |      0 | 33012    |    2.9899e-05  |       5e+06       |       4882.81     |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |        QD/I |        QD/C |        IBCB |        IBCA |        IACB |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|---------------:|------:|------------:|------------:|------------:|------------:|------------:|---------------:|------------------:|------------------:|
| count |   1211    |     1211    |   1211           | 1211           |  1211 | 1211        | 1211        | 1211        | 1211        | 1211        | 1211           |    1211           |       1211        |
| mean  |   2008.28 |     1355.45 | 582567           |    2.14382e+11 |     3 |    0.391412 |    0.388935 |    0.212221 |    0.179191 |    0.109827 |    2.00828e-06 |       2.04088e+06 |       1993.05     |
| std   |   4708.74 |     3749.07 | 583555           |    9.75922e+10 |     0 |    0.854966 |    0.834094 |    0.669562 |    0.501333 |    0.406957 |    4.70874e-06 |       1.48961e+06 |       1454.7      |
| min   |     10    |        0    |   1536           |    5.57879e+08 |     3 |    0        |    0        |    0        |   -1        |    0        |    1e-08       |     197.047       |          0.192428 |
| 25%   |     69    |       68    | 262144           |    1.75703e+11 |     3 |    0        |    0        |    0        |    0        |    0        |    6.9e-08     |  348192           |        340.031    |
| 50%   |    123    |       78    | 262144           |    2.55313e+11 |     3 |    0        |    0        |    0        |    0        |    0        |    1.23e-07    |       2.079e+06   |       2030.28     |
| 75%   |    898.5  |      533.5  |      1.04858e+06 |    2.57406e+11 |     3 |    1        |    1        |    0        |    0        |    0        |    8.985e-07   |       3.57143e+06 |       3487.72     |
| max   |  29899    |    28323    |      2.09715e+06 |    3.75918e+11 |     3 |    7        |    7        |    7        |    5        |    4        |    2.9899e-05  |       5e+06       |       4882.81     |

### IOPS and Throughput Calculations

Total duration of the session: 3.98 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 304.496 |

IOPS per IO type
| IO Type   |       0 |
|:----------|--------:|
| Diskread  | 149.859 |
| Diskwrite | 154.637 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       2.04088e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  874077           |
| Diskwrite |       3.17164e+06 |

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
| Diskwrite |     615 |
| Diskread  |     596 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |    1211 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

