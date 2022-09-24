import pm4py
from pm4py.objects.log.obj import EventLog

from datetime import datetime

def filter_log_by_demand(log: EventLog, demand_type: str):
    filtered_log = pm4py.filter_event_attribute_values(log, "tp_demanda", [demand_type], level="case", retain=True)
    return filtered_log

def filter_log_by_cliente(log: EventLog, cliente_filter: str):
    filtered_log = EventLog()
    # filtered_log.attributes = log.attributes
    for trace in log:
        cliente = trace.attributes['cliente']
        if cliente == cliente_filter:
            filtered_log.append(trace)
    return filtered_log

def filter_log_by_data(log: EventLog, start_date: datetime, end_date: datetime):
    filtered_log = EventLog()
    
    for trace in log:
        date_last_event = (trace[-1])["dt_fim"]
        date_last_event = date_last_event.to_pydatetime()
        if( start_date < date_last_event < end_date):
            filtered_log.append(trace)
    if (len(filtered_log) < 1):
        return len(log)

    return filtered_log

# Filtro cliente
def get_standard_client(log):
    clientes_count = {}
    for trace in log:
        cliente = trace.attributes['cliente']
        if cliente not in clientes_count:
            clientes_count[cliente] = 0
        clientes_count[cliente] += 1
    max_key = max(clientes_count, key = clientes_count.get)
    return max_key

# filtro demanda

def get_standard_demanda(log):
    demandas = pm4py.get_event_attribute_values(log, "tp_demanda")
    max_key = max(demandas, key = demandas.get)
    return max_key

def get_demandas(log):
    demandas = pm4py.get_event_attribute_values(log, "tp_demanda")
    return demandas