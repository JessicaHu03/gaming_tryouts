# Starting EDA for The Last Of Us Part I

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 147824 entries, 0 to 147823
   Data columns (total 21 columns):
    #   Column               Non-Null Count   Dtype  
   ---  ------               --------------   -----  
    0   IO Type              147824 non-null  object 
    1   Start Time           147824 non-null  int64  
    2   End Time             147824 non-null  int64  
    3   IO Time              147824 non-null  int64  
    4   Disk SrvT            147824 non-null  int64  
    5   IO Size              147824 non-null  int64  
    6   Byte Offset          147824 non-null  int64  
    7   Pri                  147824 non-null  int64  
    8   QD/I                 147824 non-null  int64  
    9   QD/C                 147824 non-null  int64  
    10  IBCB                 147824 non-null  int64  
    11  IBCA                 147824 non-null  int64  
    12  IACB                 147824 non-null  int64  
    13  Process Name ( PID)  147824 non-null  object 
    14  Disk                 147824 non-null  int64  
    15  Filename             147824 non-null  object 
    16  Process Name         147824 non-null  object 
    17  PID                  147824 non-null  int64  
    18  Duration_s           147824 non-null  float64
    19  Throughput_MB_s      147824 non-null  float64
    20  Throughput_GB_s      147824 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 23.7+ MB
   

## Processed Data Description
|       |       Start Time |         End Time |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |          IBCB |           IBCA |           IACB |             Disk |      PID |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------------:|-----------------:|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|--------------:|---------------:|---------------:|-----------------:|---------:|-----------------:|------------------:|------------------:|
| count | 147824           | 147824           | 147824     | 147824      | 147824           | 147824           | 147824 | 147824        | 147824        | 147824        | 147824         | 147824         | 147824           | 147824   | 147824           |  147824           |     147824        |
| mean  |      8.02989e+08 |      8.02989e+08 |    107.498 |     89.7927 |  82849.6         |      6.30563e+11 |      3 |      0.301122 |      0.302508 |      0.247808 |      0.0533134 |      0.0436668 |      1.35296e-05 |  10256.1 |      1.07498e-07 |       1.38682e+06 |       1354.32     |
| std   |      1.04417e+09 |      1.04417e+09 |    134.069 |    103.89   |  78204.3         |      1.14208e+11 |      0 |      0.69851  |      0.710357 |      0.596041 |      0.292635  |      0.286565  |      0.00367825  |  12231.5 |      1.34069e-07 |       1.23615e+06 |       1207.18     |
| min   |      5.85167e+06 |      5.8517e+06  |     10     |      0      |    512           |      5.75107e+08 |      3 |      0        |      0        |      0        |     -2         |      0         |      0           |      4   |      1e-08       |     263.012       |          0.256847 |
| 25%   |      7.32544e+07 |      7.32544e+07 |     40     |     36      |  32768           |      6.44352e+11 |      3 |      0        |      0        |      0        |      0         |      0         |      0           |      4   |      4e-08       |  271739           |        265.37     |
| 50%   |      8.09783e+07 |      8.09784e+07 |     78     |     50      |  65536           |      6.56557e+11 |      3 |      0        |      0        |      0        |      0         |      0         |      0           |      4   |      7.8e-08     |  781250           |        762.939    |
| 75%   |      1.46323e+09 |      1.46323e+09 |    135     |    117      | 131072           |      6.832e+11   |      3 |      0        |      0        |      0        |      0         |      0         |      0           |  25544   |      1.35e-07    |       2.60417e+06 |       2543.13     |
| max   |      3.14397e+09 |      3.14397e+09 |  14852     |   3532      |      2.09715e+06 |      1.57613e+12 |      3 |     57        |     69        |     34        |     23         |     15         |      1           |  32288   |      1.4852e-05  |       6.17284e+06 |       6028.16     |

## Description of Selected Columns
|       |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |          IBCB |           IBCA |           IACB |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|--------------:|---------------:|---------------:|-----------------:|------------------:|------------------:|
| count | 147824     | 147824      | 147824           | 147824           | 147824 | 147824        | 147824        | 147824        | 147824         | 147824         | 147824           |  147824           |     147824        |
| mean  |    107.498 |     89.7927 |  82849.6         |      6.30563e+11 |      3 |      0.301122 |      0.302508 |      0.247808 |      0.0533134 |      0.0436668 |      1.07498e-07 |       1.38682e+06 |       1354.32     |
| std   |    134.069 |    103.89   |  78204.3         |      1.14208e+11 |      0 |      0.69851  |      0.710357 |      0.596041 |      0.292635  |      0.286565  |      1.34069e-07 |       1.23615e+06 |       1207.18     |
| min   |     10     |      0      |    512           |      5.75107e+08 |      3 |      0        |      0        |      0        |     -2         |      0         |      1e-08       |     263.012       |          0.256847 |
| 25%   |     40     |     36      |  32768           |      6.44352e+11 |      3 |      0        |      0        |      0        |      0         |      0         |      4e-08       |  271739           |        265.37     |
| 50%   |     78     |     50      |  65536           |      6.56557e+11 |      3 |      0        |      0        |      0        |      0         |      0         |      7.8e-08     |  781250           |        762.939    |
| 75%   |    135     |    117      | 131072           |      6.832e+11   |      3 |      0        |      0        |      0        |      0         |      0         |      1.35e-07    |       2.60417e+06 |       2543.13     |
| max   |  14852     |   3532      |      2.09715e+06 |      1.57613e+12 |      3 |     57        |     69        |     34        |     23         |     15         |      1.4852e-05  |       6.17284e+06 |       6028.16     |

### IOPS and Throughput Calculations

Total duration of the session: 3.14 seconds

IOPS per disk
|   Disk |            0 |
|-------:|-------------:|
|      0 | 47105.3      |
|      1 |     0.637324 |

IOPS per IO type
| IO Type   |         0 |
|:----------|----------:|
| Diskread  | 46183     |
| Diskwrite |   922.845 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.38684e+06 |
|      1 |  114402           |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.37059e+06 |
| Diskwrite |       2.19895e+06 |

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
| Diskread  |  144928 |
| Diskwrite |    2896 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |  147822 |
|      1 |       2 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

