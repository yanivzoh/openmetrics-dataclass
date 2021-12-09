from typing import List, Optional, Union
from dataclasses import dataclass

Timestamp = int


@dataclass
class Label:
    name: str
    value: str


@dataclass
class State:
    enabled: bool
    name: str


@dataclass
class Quantile:
    quantile: float
    value: float


@dataclass
class Exemplar:
    value: float
    timestamp: Optional[Timestamp]
    label: Optional[List[Label]]


@dataclass
class Bucket:
    count: int
    upper_bound: Optional[float]
    exemplar: Optional[Exemplar]


@dataclass
class UnknownValue:
    value: Union[float, int]


@dataclass
class GaugeValue:
    value: Union[float, int]


@dataclass
class CounterValue:
    total: Union[float, int]
    created: Optional[Timestamp]
    exemplar: Optional[Exemplar]


@dataclass
class HistogramValue:
    sum: Optional[Union[float, int]]
    count: Optional[int]
    created: Optional[Timestamp]
    buckets: Optional[List[Bucket]]


@dataclass
class StateSetValue:
    states: Optional[List[State]]


@dataclass
class InfoValue:
    info: Optional[List[Label]]


@dataclass
class SummaryValue:
    sum: Optional[Union[float, int]]
    count: Optional[int]
    created: Optional[Timestamp]
    quantile: Optional[List[Quantile]]


@dataclass
class MetricPoint:
    value: Union[UnknownValue, GaugeValue, CounterValue, HistogramValue, StateSetValue, InfoValue, SummaryValue]
    timestamp: Optional[Timestamp]


@dataclass
class Metric:
    labels: Optional[List[Label]]
    metric_points: Optional[List[MetricPoint]]
