# Starting EDA for Cyberpunk 2077 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 281026 entries, 0 to 281025
   Data columns (total 21 columns):
    #   Column               Non-Null Count   Dtype  
   ---  ------               --------------   -----  
    0   IO Type              281026 non-null  object 
    1   Start Time           281026 non-null  int64  
    2   End Time             281026 non-null  int64  
    3   IO Time              281026 non-null  int64  
    4   Disk SrvT            281026 non-null  int64  
    5   IO Size              281026 non-null  int64  
    6   Byte Offset          281026 non-null  int64  
    7   Pri                  281026 non-null  int64  
    8   QD/I                 281026 non-null  int64  
    9   QD/C                 281026 non-null  int64  
    10  IBCB                 281026 non-null  int64  
    11  IBCA                 281026 non-null  int64  
    12  IACB                 281026 non-null  int64  
    13  Process Name ( PID)  281026 non-null  object 
    14  Disk                 281026 non-null  int64  
    15  Filename             281026 non-null  object 
    16  Process Name         281026 non-null  object 
    17  PID                  281026 non-null  int64  
    18  Duration_s           281026 non-null  float64
    19  Throughput_MB_s      281026 non-null  float64
    20  Throughput_GB_s      281026 non-null  float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 45.0+ MB
   

## Processed Data Description
|       |       Start Time |         End Time |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |          IBCB |           IBCA |          IACB |          Disk |       PID |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------------:|-----------------:|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|--------------:|---------------:|--------------:|--------------:|----------:|-----------------:|------------------:|------------------:|
| count | 281026           | 281026           | 281026     |  281026     | 281026           | 281026           | 281026 | 281026        | 281026        | 281026        | 281026         | 281026        | 281026        | 281026    | 281026           |  281026           |   281026          |
| mean  |      1.63506e+09 |      1.63506e+09 |    436.117 |     288.492 | 134846           |      4.05068e+11 |      3 |      0.411339 |      0.389412 |      0.379086 |      0.0322532 |      0.044519 |      1.54375  |  19101.1  |      4.36117e-07 |  387646           |      378.56       |
| std   |      2.22779e+09 |      2.22779e+09 |   2142.21  |     816.927 | 264659           |      2.18257e+11 |      0 |      6.33957  |      5.87695  |      6.17848  |      0.459771  |      0.590835 |      0.610907 |   8147.51 |      2.14221e-06 |  501926           |      490.162      |
| min   |      3.66468e+06 |      3.66529e+06 |     10     |       0     |    512           |      4.24698e+08 |      3 |      0        |      0        |      0        |     -3         |      0        |      0        |      4    |      1e-08       |       8.23686     |        0.00804381 |
| 25%   |      1.47785e+08 |      1.47785e+08 |    134     |     125     |  12288           |      2.00862e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      1        |  22412    |      1.34e-07    |   77351.5         |       75.5386     |
| 50%   |      1.49945e+09 |      1.49945e+09 |    210     |     195     |  36864           |      5.22116e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      2        |  22412    |      2.1e-07     |  173611           |      169.542      |
| 75%   |      1.72786e+09 |      1.72786e+09 |    350     |     317     | 131072           |      5.41074e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      2        |  22412    |      3.5e-07     |  506668           |      494.793      |
| max   |      1.25196e+10 |      1.25196e+10 |  79942     |   68970     |      2.09715e+06 |      1.43679e+12 |      3 |    302        |    302        |    298        |     59         |     36        |      2        |  28764    |      7.9942e-05  |       6.09741e+06 |     5954.5        |

## Description of Selected Columns
|       |    IO Time |   Disk SrvT |          IO Size |      Byte Offset |    Pri |          QD/I |          QD/C |          IBCB |           IBCA |          IACB |       Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|-----------:|------------:|-----------------:|-----------------:|-------:|--------------:|--------------:|--------------:|---------------:|--------------:|-----------------:|------------------:|------------------:|
| count | 281026     |  281026     | 281026           | 281026           | 281026 | 281026        | 281026        | 281026        | 281026         | 281026        | 281026           |  281026           |   281026          |
| mean  |    436.117 |     288.492 | 134846           |      4.05068e+11 |      3 |      0.411339 |      0.389412 |      0.379086 |      0.0322532 |      0.044519 |      4.36117e-07 |  387646           |      378.56       |
| std   |   2142.21  |     816.927 | 264659           |      2.18257e+11 |      0 |      6.33957  |      5.87695  |      6.17848  |      0.459771  |      0.590835 |      2.14221e-06 |  501926           |      490.162      |
| min   |     10     |       0     |    512           |      4.24698e+08 |      3 |      0        |      0        |      0        |     -3         |      0        |      1e-08       |       8.23686     |        0.00804381 |
| 25%   |    134     |     125     |  12288           |      2.00862e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      1.34e-07    |   77351.5         |       75.5386     |
| 50%   |    210     |     195     |  36864           |      5.22116e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      2.1e-07     |  173611           |      169.542      |
| 75%   |    350     |     317     | 131072           |      5.41074e+11 |      3 |      0        |      0        |      0        |      0         |      0        |      3.5e-07     |  506668           |      494.793      |
| max   |  79942     |   68970     |      2.09715e+06 |      1.43679e+12 |      3 |    302        |    302        |    298        |     59         |     36        |      7.9942e-05  |       6.09741e+06 |     5954.5        |

### IOPS and Throughput Calculations

Total duration of the session: 12.52 seconds

IOPS per disk
|   Disk |        0 |
|-------:|---------:|
|      0 |  1404.69 |
|      1 |  7434.99 |
|      2 | 13613.7  |

IOPS per IO type
| IO Type   |          0 |
|:----------|-----------:|
| Diskread  | 22407.8    |
| Diskwrite |    45.6218 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.06161e+06 |
|      1 |  259205           |
|      2 |  388251           |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |  385800           |
| Diskwrite |       1.29417e+06 |

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
| Diskread  |  280455 |
| Diskwrite |     571 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      2 |  170389 |
|      1 |   93056 |
|      0 |   17581 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

