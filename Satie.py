#!/usr/bin/env python
# coding: utf-8

# # アレンジ作品
# 「Performance RNN」を使ってSatieのジムノペディをモチーフにしたアレンジを作りました。

# ## ライブラリのインストール

# In[ ]:


get_ipython().system('apt-get update -qq && apt-get install -qq libfluidsynth1 fluid-soundfont-gm build-essential libasound2-dev libjack-dev')
get_ipython().system('pip install -qU pyfluidsynth pretty_midi')
get_ipython().system('pip install -qU magenta')


# ## 出だしの音を楽譜から読み取り手入力しました
# 
# イメージにある楽器（木琴）を選びました  
# 

# In[ ]:


import magenta
import note_seq
from note_seq.protobuf import music_pb2

seed = music_pb2.NoteSequence()  # NoteSequence
pg1 = 11  # 楽器の種類 -ここを変更-


# notesにnoteを追加
seed.notes.add(pitch=66, start_time=0.0, end_time=0.4, velocity=80, program=pg1)
seed.notes.add(pitch=69, start_time=0.4, end_time=0.8, velocity=80, program=pg1)
seed.notes.add(pitch=67, start_time=0.8, end_time=1.2, velocity=80, program=pg1)
seed.notes.add(pitch=66, start_time=1.2, end_time=1.6, velocity=80, program=pg1)
seed.notes.add(pitch=61, start_time=1.6, end_time=2.0, velocity=80, program=pg1)
seed.notes.add(pitch=59, start_time=2.0, end_time=2.4, velocity=80, program=pg1)
seed.notes.add(pitch=61, start_time=2.4, end_time=2.8, velocity=80, program=pg1)
seed.notes.add(pitch=62, start_time=2.8, end_time=3.2, velocity=80, program=pg1)
seed.notes.add(pitch=57, start_time=3.2, end_time=4.4, velocity=80, program=pg1)

seed.total_time = 4.4  # 所要時間
seed.tempos.add(qpm=75);  # 曲のテンポを指定

note_seq.plot_sequence(seed)  # NoteSequenceの可視化
note_seq.play_sequence(seed, synth=note_seq.fluidsynth)  # NoteSequenceの再生


# ## Performance RNNの初期化

# In[ ]:


from magenta.models.performance_rnn import performance_sequence_generator
from magenta.models.shared import sequence_generator_bundle

# モデルの初期化
note_seq.notebook_utils.download_bundle("performance_with_dynamics.mag", "/models/")  # Bundle（.magファイル）をダウンロード
bundle = sequence_generator_bundle.read_bundle_file("/models/performance_with_dynamics.mag")  # Bundleの読み込み
generator_map = performance_sequence_generator.get_generator_map()
performance_rnn = generator_map["performance_with_dynamics"](checkpoint=None, bundle=bundle)  # 生成器の設定
performance_rnn.initialize()  # 初期化


# ## 曲の生成
# 
# ランダム度合いは色々試してみて結局1にしました。
# 曲の長さはとりあえず30 秒に設定。

# In[ ]:


from note_seq.protobuf import generator_pb2

total_time = 30 # 曲の長さ（秒）
temperature = 1.0 # 曲の「ランダム度合い」を決める定数

base_end_time = max(note.end_time for note in seed.notes)  #ベース曲の終了時刻

# 生成器に関する設定
generator_options = generator_pb2.GeneratorOptions()  # 生成器のオプション
generator_options.args["temperature"].float_value = temperature  # ランダム度合い
generator_options.generate_sections.add(
    start_time=base_end_time,  # 作曲開始時刻
    end_time=total_time)  # 作曲終了時刻

# 曲の生成
gen_seq = performance_rnn.generate(seed, generator_options)
#gen_seq = performance_rnn.generate(seed, generator_options)
#gen_seq = performance_rnn.generate(seed, generator_options)
note_seq.plot_sequence(gen_seq)  # NoteSequenceの可視化
note_seq.play_sequence(gen_seq, synth=note_seq.fluidsynth)  # NoteSequenceの再生


# ## MIDIファイルの保存とダウンロード

# 

# In[ ]:





# In[ ]:




