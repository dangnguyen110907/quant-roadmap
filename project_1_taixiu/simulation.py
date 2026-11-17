"""
PROJECT 1: MÔ PHỎNG TÀI XỈU 100.000 VÁN (MONTE CARLO SIMULATION)
Mã nguồn do chính bạn đang tự tay xây dựng.
"""

from turtle import title

import matplotlib.pyplot as plt
import random


def roll_dice() -> tuple[int, int, int]:
    """Tung 3 con xúc xắc ngẫu nhiên (1-6)."""
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)


def evaluate_round(d1: int, d2: int, d3: int, bet_choice: str) -> int:
    """Xác định kết quả ván cược: Thắng (+1), Thua (-1)."""
    if d1 == d2 == d3:
        return -1
    total = d1 + d2 + d3
    if total >= 4 and total <= 10 and bet_choice == "XIU":
        return 1
    elif total >= 11 and total <= 17 and bet_choice == "TAI":
        return 1
    else:
        return -1


def simulate_player(
    initial_capital: float, bet_amount: float, rounds: int
) -> list[float]:
    """Mô phỏng 1 người chơi qua nhiều ván cược."""
    capital = initial_capital
    history = [capital]
    for i in range(rounds):
        if capital < bet_amount:
            break
        if capital >= 20000:
            break  # ĐÃ NHÂN ĐÔI VỐN -> CHỐT LỜI, CẦM TIỀN VỀ!
        choice = random.choice(["TAI", "XIU"])
        d1, d2, d3 = roll_dice()
        result = evaluate_round(d1, d2, d3, choice)
        if result == 1:
            capital += bet_amount
        else:
            capital -= bet_amount
        history.append(capital)

    return history


def simulate_all_players(
    num_player: int, initial_capital: float, bet_amount: float, rounds: int
):
    all_histories = []
    bankrupt_count = 0
    for i in range(num_player):
        all_histories.append(simulate_player(initial_capital, bet_amount, rounds))
        if all_histories[i][-1] < bet_amount:
            bankrupt_count += 1
    return all_histories, bankrupt_count


def plot_results(all_histories):
    for h in all_histories:
        plt.plot(h, color="blue", alpha=0.2)
    plt.title("đường vốn")
    plt.xlabel("số ván chơi")
    plt.ylabel("số dư tài khoản")
    plt.savefig("project_1_taixiu/equity_curve.png")
    plt.close()


def analyze_survivors(all_histories, initial_capital, bet_amount):
    survivors = []
    for h in all_histories:
        if h[-1] > bet_amount:
            survivors.append(h[-1])
    num_survivor = len(survivors)
    max_survivor = max(survivors)
    min_survivor = min(survivors)
    count_profit = 0
    for i in survivors:
        if i > initial_capital:
            count_profit += 1
    return survivors, num_survivor, max_survivor, min_survivor, count_profit


def main():
    print("Mô phỏng 100 người chơi")
    all_histories, bank_rupt = simulate_all_players(100, 10000, 1000, 5000)
    print(f"Số người cháy túi: {bank_rupt}")

    print("Vẽ biểu đồ...")
    plot_results(all_histories)
    print("vẽ xong")
    survivors, num_survivor, max_survivor, min_survivor, count_profit = (
        analyze_survivors(all_histories, 10000, 1000)
    )
    print("\n--- THỐNG KÊ NHÓM SỐNG SÓT ---")
    print(f"• Số người còn sống sót: {num_survivor}/100")
    print(f"• Số người thực sự có LÃI (> 10,000): {count_profit} người")
    print(f"• Người kiếm nhiều tiền nhất: {max_survivor:,}")
    print(f"• Người sống sót ít tiền nhất: {min_survivor:,}")


if __name__ == "__main__":
    main()
