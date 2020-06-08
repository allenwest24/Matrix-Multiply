// Implement matrix multiply in Java
// Be sure to add some mechanism to time the experiment result.

class Matrix {
  static int N = 1024;
  static double[][] A = new double[N][N];
  static double[][] B = new double[N][N];
  static double[][] C = new double[N][N];

  public static void main(String[] args) {

    // Start our timers
    double start, end;
    start = System.currentTimeMillis();

    // Initialize array
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        A[i][j] = Math.random();
        B[i][j] = Math.random();
        C[i][j] = Math.random();
      }
    }

    // Perform multiplication
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        for (int k = 0; k < N; ++k) {
          C[i][j] += A[i][k] * B[k][j];
        }
      }
    }

    end = System.currentTimeMillis();
    System.out.println(String.valueOf((end - start) / 1000));
  }
}
