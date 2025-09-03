#function to refactor
def process_data_raw(d):
  result = {}
  for i in range(len(d)):
    if d[i]['type'] == 'A':
      if 'processed' not in result:
        result['processed'] = []
      v = d[i]['value'] * 2
      if v > 100:
        result['processed'].append(v)
    elif d[i]['type'] == 'B':
      if 'special' not in result:
        result['special'] = []
      if d[i]['value'] % 2 == 0:
        result['special'].append(d[i]['value'])
  
  # Compute average for type A
  sum_a = 0
  count_a = 0
  for i in range(len(d)):
    if d[i]['type'] == 'A':
      sum_a += d[i]['value']
      count_a += 1
  if count_a > 0:
    result['avg_a'] = sum_a / count_a
  
  # Compute total for type B
  total_b = 0
  for i in range(len(d)):
    if d[i]['type'] == 'B':
      total_b += d[i]['value']
  result['total_b'] = total_b
  
  return result
