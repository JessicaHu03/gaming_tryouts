# Starting EDA for Deadlock 60M 2025-05-01 Combined

# Processed Data Overview

## Processed Data Info
<class 'pandas.core.frame.DataFrame'>
   RangeIndex: 1119 entries, 0 to 1118
   Data columns (total 21 columns):
    #   Column               Non-Null Count  Dtype  
   ---  ------               --------------  -----  
    0   IO Type              1119 non-null   object 
    1   Start Time           1119 non-null   int64  
    2   End Time             1119 non-null   int64  
    3   IO Time              1119 non-null   int64  
    4   Disk SrvT            1119 non-null   int64  
    5   IO Size              1119 non-null   int64  
    6   Byte Offset          1119 non-null   int64  
    7   Pri                  1119 non-null   int64  
    8   QD/I                 1119 non-null   int64  
    9   QD/C                 1119 non-null   int64  
    10  IBCB                 1119 non-null   int64  
    11  IBCA                 1119 non-null   int64  
    12  IACB                 1119 non-null   int64  
    13  Process Name ( PID)  1119 non-null   object 
    14  Disk                 1119 non-null   int64  
    15  Filename             1119 non-null   object 
    16  Process Name         1119 non-null   object 
    17  PID                  1119 non-null   int64  
    18  Duration_s           1119 non-null   float64
    19  Throughput_MB_s      1119 non-null   float64
    20  Throughput_GB_s      1119 non-null   float64
   dtypes: float64(3), int64(14), object(4)
   memory usage: 183.7+ KB
   

## Processed Data Description
|       |     Start Time |       End Time |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |        QD/I |        QD/C |         IBCB |         IBCA |         IACB |   Disk |      PID |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|---------------:|---------------:|----------:|------------:|-----------------:|---------------:|------:|------------:|------------:|-------------:|-------------:|-------------:|-------:|---------:|---------------:|------------------:|------------------:|
| count | 1119           | 1119           |   1119    |     1119    |   1119           | 1119           |  1119 | 1119        | 1119        | 1119         | 1119         | 1119         |   1119 |  1119    | 1119           |    1119           |       1119        |
| mean  |    2.8184e+08  |    2.81842e+08 |   1865.77 |     1484.4  | 393693           |    2.50675e+11 |     3 |    0.133155 |    0.145666 |    0.0929401 |    0.0402145 |    0.0536193 |      0 | 15687.3  |    1.86577e-06 |       1.92212e+06 |       1877.07     |
| std   |    5.9603e+08  |    5.96032e+08 |   4581.66 |     3986.88 | 458300           |    8.83146e+10 |     0 |    0.426283 |    0.462606 |    0.354292  |    0.21812   |    0.381578  |      0 |  6572.32 |    4.58166e-06 |       1.57221e+06 |       1535.36     |
| min   |    1.33962e+07 |    1.33963e+07 |     10    |        0    |   1024           |    1.18484e+09 |     3 |    0        |    0        |    0         |    0         |    0         |      0 |     4    |    1e-08       |     632.161       |          0.617345 |
| 25%   |    2.67482e+07 |    2.67483e+07 |     69    |       69    |  65536           |    1.78863e+11 |     3 |    0        |    0        |    0         |    0         |    0         |      0 | 19308    |    6.9e-08     |  190477           |        186.013    |
| 50%   |    2.7126e+07  |    2.71261e+07 |     96    |       90    | 262144           |    2.5534e+11  |     3 |    0        |    0        |    0         |    0         |    0         |      0 | 19308    |    9.6e-08     |       2.36686e+06 |       2311.39     |
| 75%   |    1.53488e+08 |    1.53492e+08 |    595.5  |      500    | 262144           |    3.10868e+11 |     3 |    0        |    0        |    0         |    0         |    0         |      0 | 19308    |    5.955e-07   |       3.52113e+06 |       3438.6      |
| max   |    2.87702e+09 |    2.87703e+09 |  28624    |    28344    |      2.09715e+06 |    3.50715e+11 |     3 |    3        |    3        |    3         |    2         |    6         |      0 | 19308    |    2.8624e-05  |       4.62963e+06 |       4521.12     |

## Description of Selected Columns
|       |   IO Time |   Disk SrvT |          IO Size |    Byte Offset |   Pri |        QD/I |        QD/C |         IBCB |         IBCA |         IACB |     Duration_s |   Throughput_MB_s |   Throughput_GB_s |
|:------|----------:|------------:|-----------------:|---------------:|------:|------------:|------------:|-------------:|-------------:|-------------:|---------------:|------------------:|------------------:|
| count |   1119    |     1119    |   1119           | 1119           |  1119 | 1119        | 1119        | 1119         | 1119         | 1119         | 1119           |    1119           |       1119        |
| mean  |   1865.77 |     1484.4  | 393693           |    2.50675e+11 |     3 |    0.133155 |    0.145666 |    0.0929401 |    0.0402145 |    0.0536193 |    1.86577e-06 |       1.92212e+06 |       1877.07     |
| std   |   4581.66 |     3986.88 | 458300           |    8.83146e+10 |     0 |    0.426283 |    0.462606 |    0.354292  |    0.21812   |    0.381578  |    4.58166e-06 |       1.57221e+06 |       1535.36     |
| min   |     10    |        0    |   1024           |    1.18484e+09 |     3 |    0        |    0        |    0         |    0         |    0         |    1e-08       |     632.161       |          0.617345 |
| 25%   |     69    |       69    |  65536           |    1.78863e+11 |     3 |    0        |    0        |    0         |    0         |    0         |    6.9e-08     |  190477           |        186.013    |
| 50%   |     96    |       90    | 262144           |    2.5534e+11  |     3 |    0        |    0        |    0         |    0         |    0         |    9.6e-08     |       2.36686e+06 |       2311.39     |
| 75%   |    595.5  |      500    | 262144           |    3.10868e+11 |     3 |    0        |    0        |    0         |    0         |    0         |    5.955e-07   |       3.52113e+06 |       3438.6      |
| max   |  28624    |    28344    |      2.09715e+06 |    3.50715e+11 |     3 |    3        |    3        |    3         |    2         |    6         |    2.8624e-05  |       4.62963e+06 |       4521.12     |

### IOPS and Throughput Calculations

Total duration of the session: 2.86 seconds

IOPS per disk
|   Disk |       0 |
|-------:|--------:|
|      0 | 390.762 |

IOPS per IO type
| IO Type   |       0 |
|:----------|--------:|
| Diskread  | 180.191 |
| Diskwrite | 210.572 |

Average throughput per disk (MB/s)
|   Disk |   Throughput_MB_s |
|-------:|------------------:|
|      0 |       1.92212e+06 |

Average throughput per IO type (MB/s)
| IO Type   |   Throughput_MB_s |
|:----------|------------------:|
| Diskread  |   483243          |
| Diskwrite |        3.1534e+06 |

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
| Diskwrite |     603 |
| Diskread  |     516 |

Value Counts for Disk:
|   Disk |   count |
|-------:|--------:|
|      0 |    1119 |

#### Pie Charts for Categorical Variables
![Pie Charts of Categorical Variables](images\categorical_pie_charts.png)

### Bivariate Analysis

#### Performance Metrics by IO Type
![Performance Metrics by IO Type](images\performance_metrics_by_io_type.png)

![IO Time per IO Type per Disk](images\io_time_per_io_type_per_disk.png)

#### IO Size vs. IO Time Log-Log Regression
![IO Size vs. IO Time Log-Log Regression](images\io_size_vs_duration_loglog.png)

![Correlation Heatmap of Key Metrics](images\correlation_heatmap.png)

