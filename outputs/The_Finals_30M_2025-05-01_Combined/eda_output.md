# Starting EDA for The Finals 30M 2025-05-01 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 57702 entries, 0 to 57701
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              57702 non-null  object 
    1   Start Time           57702 non-null  int64  
    2   End Time             57702 non-null  int64  
    3   IO Time              57702 non-null  int64  
    4   Disk SrvT            57702 non-null  int64  
    5   IO Size              57702 non-null  int64  
    6   Byte Offset          57702 non-null  int64  
    7   Pri                  57702 non-null  int64  
    8   QD/I                 57702 non-null  int64  
    9   QD/C                 57702 non-null  int64  
    10  IBCB                 57702 non-null  int64  
    11  IBCA                 57702 non-null  int64  
    12  IACB                 57702 non-null  int64  
    13  Process Name ( PID)  57702 non-null  object 
    14  Disk                 57702 non-null  int64  
    15  Filename             57702 non-null  object 
    16  Process Name         57702 non-null  object 
    17  PID                  57702 non-null  int64  
    18  Duration_s           57702 non-null  float64
    19  Throughput_MB_s      57702 non-null  float64
    20  Throughput_GB_s      57702 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 9.2+ MB
   

## Processed Data Description
|       |      Start Time |        End Time |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |           Pri |         QD/I |         QD/C |         IBCB |         IBCA |          IACB |   Disk |      PID |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------------:|----------------:|----------:|------------:|-----------------:|----------------:|--------------:|-------------:|-------------:|-------------:|-------------:|--------------:|-------:|---------:|----------------:|------------------:|------------------:|
| count | 57702           | 57702           | 57702     |   57702     |  57702           | 57702           | 57702         | 57702        | 57702        | 57702        | 57702        | 57702         |  57702 | 57702    | 57702           |   57702           |     57702         |
| mean  |     4.57342e+08 |     4.57343e+08 |   473.143 |     367.326 | 191440           |     2.85094e+11 |     2.99964   |     0.273335 |     0.272122 |     0.221569 |     0.051766 |     0.0581956 |      0 |  2950.86 |     4.73143e-07 |       1.32333e+06 |      1292.32      |
| std   |     6.04983e+08 |     6.04983e+08 |  1711.94  |    1323.93  | 207237           |     1.50615e+11 |     0.0330409 |     2.85156  |     2.85215  |     2.71437  |     0.376296 |     0.479499  |      0 |  5176.71 |     1.71194e-06 |       1.1789e+06  |      1151.27      |
| min   |     4.03567e+06 |     4.03658e+06 |    12     |       0     |    512           |     4.03702e+08 |     0         |     0        |     0        |     0        |    -1        |     0         |      0 |     4    |     1.2e-08     |      34.2738      |         0.0334705 |
| 25%   |     5.29459e+07 |     5.29461e+07 |    82     |      78     |  65536           |     2.04126e+11 |     3         |     0        |     0        |     0        |     0        |     0         |      0 |     4    |     8.2e-08     |  247036           |       241.246     |
| 50%   |     1.89828e+08 |     1.89829e+08 |   146     |     120     | 262144           |     3.5176e+11  |     3         |     0        |     0        |     0        |     0        |     0         |      0 |     4    |     1.46e-07    |       1.01351e+06 |       989.759     |
| 75%   |     9.14363e+08 |     9.1437e+08  |   215     |     184     | 262144           |     3.97218e+11 |     3         |     0        |     0        |     0        |     0        |     0         |      0 | 10756    |     2.15e-07    |       2.08333e+06 |      2034.51      |
| max   |     2.08413e+09 |     2.08413e+09 | 35151     |   35151     |      2.09715e+06 |     4.16936e+11 |     3         |   100        |   100        |    95        |    17        |    32         |      0 | 39084    |     3.5151e-05  |       5.9232e+06  |      5784.38      |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |     Byte Offset |           Pri |         QD/I |         QD/C |         IBCB |         IBCA |          IACB |      Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|----------------:|--------------:|-------------:|-------------:|-------------:|-------------:|--------------:|----------------:|------------------:|------------------:|
| count | 57702     |   57702     |  57702           | 57702           | 57702         | 57702        | 57702        | 57702        | 57702        | 57702         | 57702           |   57702           |     57702         |
| mean  |   473.143 |     367.326 | 191440           |     2.85094e+11 |     2.99964   |     0.273335 |     0.272122 |     0.221569 |     0.051766 |     0.0581956 |     4.73143e-07 |       1.32333e+06 |      1292.32      |
| std   |  1711.94  |    1323.93  | 207237           |     1.50615e+11 |     0.0330409 |     2.85156  |     2.85215  |     2.71437  |     0.376296 |     0.479499  |     1.71194e-06 |       1.1789e+06  |      1151.27      |
| min   |    12     |       0     |    512           |     4.03702e+08 |     0         |     0        |     0        |     0        |    -1        |     0         |     1.2e-08     |      34.2738      |         0.0334705 |
| 25%   |    82     |      78     |  65536           |     2.04126e+11 |     3         |     0        |     0        |     0        |     0        |     0         |     8.2e-08     |  247036           |       241.246     |
| 50%   |   146     |     120     | 262144           |     3.5176e+11  |     3         |     0        |     0        |     0        |     0        |     0         |     1.46e-07    |       1.01351e+06 |       989.759     |
| 75%   |   215     |     184     | 262144           |     3.97218e+11 |     3         |     0        |     0        |     0        |     0        |     0         |     2.15e-07    |       2.08333e+06 |      2034.51      |
| max   | 35151     |   35151     |      2.09715e+06 |     4.16936e+11 |     3         |   100        |   100        |    95        |    17        |    32         |     3.5151e-05  |       5.9232e+06  |      5784.38      |

### IOPS and Throughput Calculations

Total duration of the session: 2.08 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 27740.1 |

IOPS per IO type
| IO Type   |          0 |
|:----------|-----------:|
| Diskread  | 27668      |
| Diskwrite |    72.1121 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.32333e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.32573e+06 |
| Diskwrite |  405608           |

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
| Diskread  |   57552 |
| Diskwrite |     150 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |   57702 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

