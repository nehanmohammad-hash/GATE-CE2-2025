#include <stdio.h>

int main() {
    // 1. Given Data
    double sp = 192.0;               // Selling price per kg (₹)
    double profit_pct = 0.08;      // 8% profit
    double cp_p = 800.0 / 5.0;     // Cost price of variety P = ₹ 160/kg
    double cp_q = 800.0 / 4.0;     // Cost price of variety Q = ₹ 200/kg

    // 2. Derivation of Mixture Cost Price (CP_mix)
    // Formula: SP = CP * (1 + profit) => CP_mix = SP / (1 + profit)
    double cp_mix = sp / (1.0 + profit_pct);
    printf("Derived Mixture Cost Price (CP_mix) = %.2f ₹/kg\n", cp_mix);

    // 3. Derivation of Alligation Rule:
    // Let W_P and W_Q be weights. Total Cost = W_P * cp_p + W_Q * cp_q = (W_P + W_Q) * cp_mix
    // W_P * (cp_mix - cp_p) = W_Q * (cp_q - cp_mix)
    // W_P / W_Q = (cp_q - cp_mix) / (cp_mix - cp_p)

    double diff_q = cp_q - cp_mix;       // 200 - 177.77 = 22.22
    double diff_p = cp_mix - cp_p;       // 177.77 - 160 = 17.77

    double ratio_p_to_q = diff_q / diff_p;
    printf("Weight Ratio W_P : W_Q = %.2f / %.2f = 5 : 4\n", diff_q, diff_p);

    return 0;
}

