# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O_ETktSxrNcnoDPTPRjpiHUlvWhQObsB
"""

!pip install streamlit==1.7.0 --quiet
!pip install pyngrok==4.1.1 --quiet

import streamlit as st
from pyngrok import ngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile model.py
# # 以下を「model.py」に書き込み
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from torchvision import models, transforms
# from PIL import Image
# 
# classes_ja = ["飛行機", "自動車", "鳥", "猫", "鹿", "犬", "カエル", "馬", "船", "トラック"]
# classes_en = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
# n_class = len(classes_ja)
# img_size = 32
# 
# # CNNのモデル
# class Net(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = nn.Conv2d(3, 6, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         self.fc1 = nn.Linear(16*5*5, 256)
#         self.dropout = nn.Dropout(p=0.5)
#         self.fc2 = nn.Linear(256, 10)
# 
#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = x.view(-1, 16*5*5)
#         x = F.relu(self.fc1(x))
#         x = self.dropout(x)
#         x = self.fc2(x)
#         return x
# 
# def predict(img):
#     # モデルへの入力
#     img = img.convert("RGB")
#     img = img.resize((img_size, img_size))
#     transform = transforms.Compose([transforms.ToTensor(),
#                                     transforms.Normalize((0.0, 0.0, 0.0), (1.0, 1.0, 1.0))  # 平均値を0、標準偏差を1に
#                                 ])
#     img = transform(img)
#     x = img.reshape(1, 3, img_size, img_size)
# 
#     # 訓練済みモデル
#     net = Net()
#     net.load_state_dict(torch.load(
#         "model_cnn.pth", map_location=torch.device("cpu")
#         ))
#     
#     # 予測
#     net.eval()
#     y = net(x)
#     
#    # 結果を返す
#     y_prob = torch.nn.functional.softmax(torch.squeeze(y))  # 確率で表す
#     sorted_prob, sorted_indices = torch.sort(y_prob, descending=True)  # 降順にソート
#     return [(classes_ja[idx], classes_en[idx], prob.item()) for idx, prob in zip(sorted_indices, sorted_prob)]

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# # 以下を「app.py」に書き込み
# import streamlit as st
# import matplotlib.pyplot as plt
# from PIL import Image
# from model import predict
# 
# st.set_option("deprecation.showfileUploaderEncoding", False)
# 
# st.sidebar.title("画像認識アプリ")
# st.sidebar.write("オリジナルの画像認識モデルを使って何の画像かを判定します。")
# 
# st.sidebar.write("")
# 
# img_source = st.sidebar.radio("画像のソースを選択してください。",
#                               ("画像をアップロード", "カメラで撮影"))
# if img_source == "画像をアップロード":
#     img_file = st.sidebar.file_uploader("画像を選択してください。", type=["png", "jpg"])
# elif img_source == "カメラで撮影":
#     img_file = st.camera_input("カメラで撮影")
# 
# if img_file is not None:
#     with st.spinner("推定中..."):
#         img = Image.open(img_file)
#         st.image(img, caption="対象の画像", width=480)
#         st.write("")
# 
#         # 予測
#         results = predict(img)
# 
#         # 結果の表示
#         st.subheader("判定結果")
#         n_top = 3  # 確率が高い順に3位まで返す
#         for result in results[:n_top]:
#             st.write(str(round(result[2]*100, 2)) + "%の確率で" + result[0] + "です。")
# 
#         # 円グラフの表示
#         pie_labels = [result[1] for result in results[:n_top]]
#         pie_labels.append("others")
#         pie_probs = [result[2] for result in results[:n_top]]
#         pie_probs.append(sum([result[2] for result in results[n_top:]]))
#         fig, ax = plt.subplots()
#         wedgeprops={"width":0.3, "edgecolor":"white"}
#         textprops = {"fontsize":6}
#         ax.pie(pie_probs, labels=pie_labels, counterclock=False, startangle=90,
#                textprops=textprops, autopct="%.2f", wedgeprops=wedgeprops)  # 円グラフ
#         st.pyplot(fig)

!ngrok authtoken 2JzPGkJp84xpgDrIPmLaFTd0GH8_47bgtjdZcdfc4eZoeAv5o

!streamlit run app.py &>/dev/null&  # 「&>/dev/null&」により、出力を非表示にしてバックグランドジョブとして実行

ngrok.kill()  # プロセスの修了
url = ngrok.connect(port="2000")  # 接続

print(url)

import streamlit
import torch
import torchvision
import PIL
import matplotlib

print("streamlit==" + streamlit.__version__)
print("torch==" + torch.__version__)
print("torchvision==" + torchvision.__version__)
print("Pillow==" + PIL.__version__)
print("matplotlib==" + matplotlib.__version__)

with open("requirements.txt", "w") as w:
    w.write("streamlit==1.8.1\n")  # Streamlit Cloud上で動作が確認できたバージョン
    w.write("torch==1.10.0\n")  # Cuda対応は要らないのでcu111は記述しない
    w.write("torchvision==0.11.1\n")  # Cuda対応は要らないのでcu111は記述しない
    w.write("Pillow\n")
    w.write("matplotlib\n")