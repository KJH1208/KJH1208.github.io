import numpy as np
import pickle

def generate_random_dataset(N, d, R, alpha):
    # 1. True 파라미터 w와 b 생성
    w_true = np.random.uniform(-R, R, d)
    b_true = np.random.uniform(-R, R)

    # 2. 데이터셋 생성
    X = np.random.uniform(-R, R, (N, d))
    noise = np.random.normal(0, alpha * R, N)
    y = X.dot(w_true) + b_true + noise

    # 3. 데이터셋 분할
    train_size = int(0.85 * N)
    dev_size = int(0.05 * N)
    test_size = N - train_size - dev_size

    X_train, y_train = X[:train_size], y[:train_size]
    X_dev, y_dev = X[train_size:train_size + dev_size], y[train_size:train_size + dev_size]
    X_test, y_test = X[train_size + dev_size:], y[train_size + dev_size:]

    # 4. 데이터셋 저장
    dataset = {
        'X_train': X_train, 'y_train': y_train,
        'X_dev': X_dev, 'y_dev': y_dev,
        'X_test': X_test, 'y_test': y_test,
        'w_true': w_true, 'b_true': b_true
    }

    with open(f'myrandomdataset_{N}.pkl', 'wb') as f:
        pickle.dump(dataset, f)

#예시
generate_random_dataset(N=1000, d=10, R=10, alpha=0.1)
generate_random_dataset(N=10000, d=10, R=10, alpha=0.1)
generate_random_dataset(N=100000, d=10, R=10, alpha=0.1)
