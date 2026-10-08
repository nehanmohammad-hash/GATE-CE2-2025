#include <stdio.h>

int main() {
    int digits[] = {1, 2, 3, 4, 5};
    int p, q, r, s, t;

    // Nested loops for each digit (ensuring uniqueness)
    for (int i = 0; i < 5; i++) {
        p = digits[i];
        for (int j = 0; j < 5; j++) {
            q = digits[j];
            if (q == p) continue;
            
            for (int k = 0; k < 5; k++) {
                r = digits[k];
                if (r == p || r == q) continue;
                
                for (int l = 0; l < 5; l++) {
                    s = digits[l];
                    if (s == p || s == q || s == r) continue;
                    
                    for (int m = 0; m < 5; m++) {
                        t = digits[m];
                        if (t == p || t == q || t == r || t == s) continue;
                        
                        // Conditions: P < Q, S > P > T, R < T
                        if (p < q && s > p && p > t && r < t) {
                            printf("P=%d, Q=%d, R=%d, S=%d, T=%d\n", p, q, r, s, t);
                        }
                    }
                }
            }
        }
    }

    return 0;
}

