# 번호 붙이기

N명의 사람에게 1에서 N까지의 번호를 하나씩 붙이려고 한다. 서로 다른 사람에게 같은 번호를 붙여서는 안되며, 각 사람은 싫어하는 수가 하나씩 있어서 싫어하는 수를 번호로 붙이면 안 된다.

이를 만족하면서 사람들에게 번호를 붙이는 방법의 개수를 구하는 프로그램을 작성하라.

**[입력]**


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.


각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤5,000)이 주어진다.

두 번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다. 각 정수는 각 사람이 싫어하는 수를 나타내며, 1 이상 5,000 이하의 정수이다. 



**[출력]**

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

각 테스트 케이스마다 사람들에게 번호를 붙이는 방법의 개수를 출력한다. 이 수가 매우 클 수 있으므로, 1,000,000,007로 나눈 나머지를 출력하도록 한다.

 

```
4  //테스트케이수 개수
3  //첫번째 사람 수
1 2 3  // 각 사람이 싫어하는 수(1, 2, 3)
3
1 4 7
5
1 1 1 1 1
4
1 3 3 4
```

```
#1 2
#2 4
#3 0
#4 8
```



풀었다!!!!!!!!

근데 파이썬으로 푸는게 없어서 왠지 뻘짓한거같네.....

그래도 열심히 인터넷으로 보고 풀었다 후우....







밑에는 C++으로 풀이



```c++
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
using lld = long long int;
using pii = pair<int, int>;
using pil = pair<int, lld>;
using pli = pair<lld, int>;
using pll = pair<lld, lld>;
using llz = long long int;
using lf = long double;
#define M 1000000007
int n, m;
lld f[100009];
int a[100009];
void inil() {
    f[0] = 1;
    for (int i = 1; i <= 5000; i++) {
        f[i] = (f[i - 1] * i) % M;
    }
}
lld d[2][5009];
int main() {
    inil();
    int t = 1, tv = 0;
    int i, j, k, l;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        sort(a, a + n);
        for (i = 0; i < n; i++) {
            if (a[i] > n)break;
        }
        m = i;
        lld res = f[n];
        int cur = 0;
        int nxt = 1;
        for (i = 0; i <= m + 1; i++) {
            d[0][i] = d[1][i] = 0;
        }
        d[0][0] = 1;
        int tm = 1;
        for (i = 0; i < m;) {
            for (j = i; j < m; j++) {
                if (a[i] != a[j])break;
            }
            d[nxt][0] = 1;
            for (k = 1; k <= tm; k++) {
                d[nxt][k] = (d[cur][k] + (j-i)*d[cur][k-1])%M;
            }
            tm++;
            i = j;
            cur ^= 1;
            nxt ^= 1;
        }
        for (i = 1; i < tm; i++) {
            lld ss = d[cur][i] * f[n - i] % M;
            if (i & 1) {
                res = (res + M - ss) % M;
            }
            else {
                res = (res + ss) % M;
            }
        }
 
        printf("#%d %lld\n", ++tv, res);
    }
}
```

