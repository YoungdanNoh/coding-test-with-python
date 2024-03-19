# 선택 정렬의 시간 복잡도 <br>
- 전체 연산 횟수 : N + (N-1) + (N-2) + ... + 2 <br>
- 따라서 빅오 표기법에 따라 O(N<sup>2</sup>)이 된다. 
    > <span style="font-size:120%">O(N<sup>2</sup>)</span>

# 삽입 정렬의 시간 복잡도 <br>
- 반복문이 2번 중첩되어 사용되기 때문에 직관적으로 O(N<sup>2</sup>)이 된다.
- 최선의 경우 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작하여 O(N)의 시간복잡도를 가진다.
    > <span style="font-size:120%">O(N<sup>2</sup>)</span> <br>
  > 최선의 경우: <span style="font-size:120%">O(N)</span>
 
# 퀵 정렬의 시간 복잡도 <br>
- 이상적인 경우 절반씩 분할이 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
- 높이 x 너비 = logN x N = NlogN
- 최악의 경우로는 이미 정렬된 데이터에 대하여 첫번째 원소를 피벗(Pivot)으로 삼을 때, 계속해서 왼쪽 데이터 하나를 제외하고 오른쪽 데이터 전부에 대해 정렬을 다시 수행하게 되므로 O(N<sup>2</sup>)이 된다.
    > 평균의 경우: <span style="font-size:120%">O(NlogN)</span> <br>
  > 최악의 경우: <span style="font-size:120%">O(N<sup>2</sup>)</span>

# 계수 정렬의 시간 복잡도 <br>
- 데이터의 범위가 작을 경우에는 O(N)이 된다.
- 데이터의 개수가 N, 양수 데이터 중 최댓값이 K일 때, 최악의 경우에도 O(N + K)를 보장한다.
    > 데이터의 범위가 작을 경우: <span style="font-size:120%">O(N)</span> <br>
  > 최악의 경우: <span style="font-size:120%">O(N + K)</span>