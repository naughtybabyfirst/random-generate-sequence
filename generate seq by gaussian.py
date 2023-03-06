import numpy as np
import random


def gen_gaussain_matrix(length):
    # 定义高斯分布的均值和标准差
    mu, sigma = 0, 0.1

    # 生成标准正态分布列向量
    gaussian_col = np.random.normal(mu, sigma, (length, 1))

    # 生成标准正态分布行向量
    gaussian_row = np.random.normal(mu, sigma, (1, length))

    # 生成高斯分布矩阵
    gaussian_mat = gaussian_col * gaussian_row

    # 对矩阵中的所有元素进行平移
    gaussian_mat -= np.min(gaussian_mat)

    # 将矩阵中所有元素的和除以1
    gaussian_mat /= np.sum(gaussian_mat)

    # 输出矩阵
    # print(len(gaussian_mat))
    return gaussian_mat


def gen_seq():
    # 原序列
    original_seq = [i for i in range(0, 33)]

    # 生成数字序列的长度
    seq_len = 6

    # 生成数字序列
    num_seq = []
    selected_num = 0
    first_selected_num = 0
    for i in range(seq_len):
        if i == 0:
            selected_num = random.choice(original_seq)
            first_selected_num = selected_num
            num_seq.append(first_selected_num)

        gaussion_mat = gen_gaussain_matrix(33)
        next_state_probs = gaussion_mat[selected_num]

        # 随机选择下一个状态
        next_state_probs /= np.sum(next_state_probs)

        selected_num = np.random.choice(original_seq, p=next_state_probs)
        if selected_num in num_seq:
            continue

        # 添加到数字序列中
        num_seq.append(selected_num)

        if len(num_seq) == 6:
            break

    return list(map(lambda x: x + 1, num_seq)), first_selected_num + 1


def gen_blue_num():
    return random.choice([i for i in range(0, 16)]) + 1


if __name__ == '__main__':
    for _ in range(5):
        res, first_selected_num = gen_seq()
        blue_num = gen_blue_num()
        print("first selected num:{0}, generate: {1} | {2}, sum: {3}".format(first_selected_num, 
                                                                             sorted(res), 
                                                                             blue_num,
                                                                             sum(res)))
