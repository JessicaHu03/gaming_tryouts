# Starting EDA for Hogwarts Legacy Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 520231 entries, 0 to 520230
   Data columns (total 21 columns):
    #   Column               Non-Null Count   Dtype  
   ---  ------               --------------   -----  
    0   IO Type              520231 non-null  object 
    1   Start Time           520231 non-null  int64  
    2   End Time             520231 non-null  int64  
    3   IO Time              520231 non-null  int64  
    4   Disk SrvT            520231 non-null  int64  
    5   IO Size              520231 non-null  int64  
    6   Byte Offset          520231 non-null  int64  
    7   Pri                  520231 non-null  int64  
    8   QD/I                 520231 non-null  int64  
    9   QD/C                 520231 non-null  int64  
    10  IBCB                 520231 non-null  int64  
    11  IBCA                 520231 non-null  int64  
    12  IACB                 520231 non-null  int64  
    13  Process Name ( PID)  520231 non-null  object 
    14  Disk                 520231 non-null  int64  
    15  Filename             520231 non-null  object 
    16  Process Name         520231 non-null  object 
    17  PID                  520231 non-null  int64  
    18  Duration_s           520231 non-null  float64
    19  Throughput_MB_s      520231 non-null  float64
    20  Throughput_GB_s      520231 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 83.4+ MB
   

## Processed Data Description
|       |       Start Time |         End Time |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |           IBCB |          IBCA |          IACB |   Disk |       PID |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------------:|-----------------:|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|---------------:|--------------:|--------------:|-------:|----------:|-----------------:|------------------:|------------------:|
| count | 520231           | 520231           | 520231     |  520231     | 520231           | 520231           | 520231 | 520231        | 520231        | 520231         | 520231        | 520231        | 520231 | 520231    | 520231           |  520231           |    520231         |
| mean  |      6.12449e+08 |      6.1245e+08  |    220.35  |     193.374 | 134752           |      8.1198e+11  |      3 |      0.273515 |      0.273252 |      0.0766756 |      0.196839 |      0.184505 |      0 |   9314.95 |      2.2035e-07  |       1.27071e+06 |      1240.93      |
| std   |      8.84593e+08 |      8.84593e+08 |    911.581 |     816.617 |      1.12727e+06 |      4.0182e+11  |      0 |      3.44383  |      3.44053  |      1.33255   |      2.95086  |      3.08349  |      0 |   9433.35 |      9.11581e-07 |       1.36171e+06 |      1329.79      |
| min   | 413739           | 413893           |      6     |       0     |    512           |      5.75103e+08 |      3 |      0        |      0        |      0         |     -1        |      0        |      0 |      4    |      6e-09       |     101.556       |         0.0991758 |
| 25%   |      2.5857e+07  |      2.58572e+07 |     16     |      15     |   8192           |      5.15063e+11 |      3 |      0        |      0        |      0         |      0        |      0        |      0 |      4    |      1.6e-08     |  325521           |       317.891     |
| 50%   |      9.99495e+07 |      9.99497e+07 |     63     |      61     |  65536           |      5.56581e+11 |      3 |      0        |      0        |      0         |      0        |      0        |      0 |  13996    |      6.3e-08     |  686813           |       670.716     |
| 75%   |      1.07963e+09 |      1.07963e+09 |    191     |     172     | 262144           |      1.20382e+12 |      3 |      0        |      0        |      0         |      0        |      0        |      0 |  16832    |      1.91e-07    |       1.73611e+06 |      1695.42      |
| max   |      3.23635e+09 |      3.23635e+09 |  62769     |   62769     |      4.03702e+08 |      1.78427e+12 |      3 |    132        |    132        |    108         |    131        |    254        |      0 |  39864    |      6.2769e-05  |       6.21544e+06 |      6069.76      |

## Description of Selected Columns
|       |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |           IBCB |          IBCA |          IACB |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|---------------:|--------------:|--------------:|-----------------:|------------------:|------------------:|
| count | 520231     |  520231     | 520231           | 520231           | 520231 | 520231        | 520231        | 520231         | 520231        | 520231        | 520231           |  520231           |    520231         |
| mean  |    220.35  |     193.374 | 134752           |      8.1198e+11  |      3 |      0.273515 |      0.273252 |      0.0766756 |      0.196839 |      0.184505 |      2.2035e-07  |       1.27071e+06 |      1240.93      |
| std   |    911.581 |     816.617 |      1.12727e+06 |      4.0182e+11  |      0 |      3.44383  |      3.44053  |      1.33255   |      2.95086  |      3.08349  |      9.11581e-07 |       1.36171e+06 |      1329.79      |
| min   |      6     |       0     |    512           |      5.75103e+08 |      3 |      0        |      0        |      0         |     -1        |      0        |      6e-09       |     101.556       |         0.0991758 |
| 25%   |     16     |      15     |   8192           |      5.15063e+11 |      3 |      0        |      0        |      0         |      0        |      0        |      1.6e-08     |  325521           |       317.891     |
| 50%   |     63     |      61     |  65536           |      5.56581e+11 |      3 |      0        |      0        |      0         |      0        |      0        |      6.3e-08     |  686813           |       670.716     |
| 75%   |    191     |     172     | 262144           |      1.20382e+12 |      3 |      0        |      0        |      0         |      0        |      0        |      1.91e-07    |       1.73611e+06 |      1695.42      |
| max   |  62769     |   62769     |      4.03702e+08 |      1.78427e+12 |      3 |    132        |    132        |    108         |    131        |    254        |      6.2769e-05  |       6.21544e+06 |      6069.76      |

### IOPS and Throughput Calculations

Total duration of the session: 3.24 seconds

IOPS per disk
|   Disk |      0 |
|-------:|-------:|
|      0 | 160767 |

IOPS per IO type
| IO Type   |        0 |
|:----------|---------:|
| Diskread  | 110326   |
| Diskwrite |  50440.7 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.27071e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |       1.65495e+06 |
| Diskwrite |  430292           |

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
Log-Normal Fit Parameters for IO Time: (0, 0, 3)

### Categorical Features Distribution

#### Value Counts for Categorical Features

Value Counts for IO Type:
| IO Type   |   count |
|:----------|--------:|
| Diskread  |  357008 |
| Diskwrite |  163223 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |  520231 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

