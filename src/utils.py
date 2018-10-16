import os
import pandas as pd
import numpy as np


def parse_num(str):
    str = str.strip()
    decimal = str.find('.')
    if len(str) == 0:
        return None
    elif decimal > 0:
        return float(str)
    else:
        return int(str)


def parse_metadata(str):
    pos = str.find('>')
    key = str[1:pos]
    return key, parse_num(str[pos + 1:])


def read_tntp_net(f):
    header = None
    data = []
    df_data = {}
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        elif line[0] == '~' and not header:
            header = line[1:].strip(' ;\t').split('\t')
            for i, name in enumerate(header):
                data.append([])
                df_data[name.strip()] = data[i]
        elif header:
            for i, num in enumerate(line.strip(' ;\t').split('\t')):
                data[i].append(parse_num(num))
    return df_data


def read_tntp_trips(f, nodes):
    df_data = np.zeros((nodes + 1, nodes + 1))
    i = 0
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        elif line.startswith('Origin'):
            i += 1
        else:
            row = line.strip(' ;\t').split(';')
            for item in row:
                key, value = item.strip().split(':')
                key = parse_num(key)
                value = parse_num(value)
                df_data[key][i] = value
    return df_data


def read_tntp(network, file, base_path=os.path.join(os.path.dirname(__file__), '..', 'tntp')):
    filename = os.path.join(base_path, network, '%s_%s.tntp' % (network, file))
    attrs = {}
    df_data = {}
    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                # Skip empty lines
                continue
            elif line[0] == '<':
                # Read Metadata
                key, value = parse_metadata(line)
                if value:
                    attrs[key] = value
                else:
                    break
        if file == 'net':
            df_data = read_tntp_net(f)
        elif file == 'trips':
            df_data = read_tntp_trips(f, attrs['NUMBER OF ZONES'])
        return pd.DataFrame(df_data), attrs


if __name__ == '__main__':
    df_net, attrs_net = read_tntp('SiouxFalls', 'net')
    df_trips, attrs_trips = read_tntp('SiouxFalls', 'trips')
