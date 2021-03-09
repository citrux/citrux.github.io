function gauss(A, b) {
    for (var i = 0; i < A.length; i++) {
        var a = A[i][i];
        for (var j = 0; j < A.length; j++) {
            A[i][j] /= a;
        }
        b[i] /= a;
        for (var k = i+1; k < A.length; k++) {
            var a = A[k][i]
            for (var j = 0; j < A.length; j++) {
                A[k][j] -= a * A[i][j];
            }
            b[k] -= a * b[i];
        }
    }

    for (var i = A.length - 1; i >= 0; i--) {
        for (var k = i-1; k >= 0; k--) {
            b[k] -= A[k][i] * b[i];
            A[k][i] = 0;
        }
    }
    return b;
}

function add(a, b) {
    return a + b;
}

function polyfit(xs, ys, degree) {
    A = d3.range(degree+1).map(i =>
            d3.range(degree+1).map(j =>
                xs.map(a => a**(i+j)).reduce(add)));
    b = d3.range(degree+1).map(i => xs.map((x, j) => ys[j] * x ** i).reduce(add));
    return gauss(A, b);
}

function polyval(poly, xs) {
    return xs.map(x => poly.map((a, i) => a * x**i).reduce(add));
}

function linspace(start, end, n) {
    result = []
    for (var i = 0; i < n; i++) {
        result.push(((n-1-i) * start + i * end) / (n-1));
    }
    return result;
}
