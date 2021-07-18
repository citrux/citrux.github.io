#include <map>
#include <cmath>
#include <iostream>

using namespace std;

typedef long long int64;

int *prime, *mu, *S;
map<int64, int64> g;
map<pair<int, int64>, int64> f;

int64 calc(int64 x) {
    if (g.count(x)) {
        return g[x];
    }
    int64 &t = g[x];
    for (int64 i = 1; i * i <= x; ++i) {
        t +=  x / i / i * mu[i];
    }
    return t;
}

int64 dfs(int i, int64 j) {
    auto x = make_pair(i, j);
    if (f.count(x)) {
        return f[x];
    }
    if ((int64)S[i] * S[i] > j) {
        return calc(j) - i;
    }
    return f[x] = 1 + dfs(i, j / S[i]) + dfs(i + 1, j);
}

int main(int argc, char **argv) {
    int64 N = atol(argv[1]);
    int64 LMT = sqrt(N);
    prime = new int[LMT + 1];
    mu = new int[LMT * 2 + 1];
    S = new int[LMT * 2];

    mu[1] = 1;
    for (int i = 2; i != LMT * 2 + 1; ++i) {
        if (prime[i] == 0) {
            prime[++prime[0]] = i;
            mu[i] = -1;
        }
        for (int j = 1; prime[j] * i <= LMT; ++j) {
            int t = i * prime[j];
            prime[t] = 1;
            if (i % prime[j] == 0) {
                mu[t] = 0;
                break;
            }
            mu[t] = -mu[i];
        }
        if (mu[i]) {
            S[++S[0]] = i;
        }
    }
    cout << dfs(1, N) << endl;
    return 0;
}
