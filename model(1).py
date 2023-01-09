
!gsutil -q -m cp -R gs://download.magenta.tensorflow.org/models/music_vae/colab2/checkpoints/mel_2bar_big.ckpt.* /content/


from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

# モデルの初期化
music_vae = TrainedModel(
      configs.CONFIG_MAP["cat-mel_2bar_big"], 
      batch_size=4,  # 一度に処理するデータ数
      checkpoint_dir_or_path="/content/mel_2bar_big.ckpt")


import note_seq

generated = music_vae.sample(n=5,  # 生成数
                             length=64,  # ステップ数
                             temperature=1.0)  # 温度

for ns in generated:
    note_seq.plot_sequence(ns)
    note_seq.play_sequence(ns, synth=note_seq.fluidsynth)


import magenta
import note_seq
from note_seq.protobuf import music_pb2

# 最初のNoteSeqence
kira2_start = music_pb2.NoteSequence()
pg = 10

#kira2_start.notes.add(pitch=62, start_time=0.0, end_time=0.4, velocity=80)
#kira2_start.notes.add(pitch=60, start_time=0.4, end_time=0.8, velocity=80)
#kira2_start.notes.add(pitch=62, start_time=0.8, end_time=1.2, velocity=80)
#kira2_start.notes.add(pitch=64, start_time=1.2, end_time=1.6, velocity=80)
#kira2_start.notes.add(pitch=67, start_time=1.6, end_time=2.0, velocity=80)
#kira2_start.notes.add(pitch=64, start_time=2.0, end_time=2.4, velocity=80)
#kira2_start.notes.add(pitch=62, start_time=2.4, end_time=3.2, velocity=80)
#kira2_start.notes.add(pitch=64, start_time=3.2, end_time=3.6, velocity=80)
#kira2_start.notes.add(pitch=67, start_time=3.6, end_time=4.0, velocity=80)
#kira2_start.notes.add(pitch=69, start_time=4.0, end_time=4.4, velocity=80)
#kira2_start.notes.add(pitch=67, start_time=4.4, end_time=4.6, velocity=80)
#kira2_start.notes.add(pitch=69, start_time=4.6, end_time=4.8, velocity=80)
#kira2_start.notes.add(pitch=74, start_time=4.8, end_time=5.2, velocity=80)
#kira2_start.notes.add(pitch=71, start_time=5.2, end_time=5.6, velocity=80)
#kira2_start.notes.add(pitch=69, start_time=5.6, end_time=6.0, velocity=80)
#kira2_start.notes.add(pitch=67, start_time=6.0, end_time=6.4, velocity=80)

kira2_start.notes.add(pitch=72, start_time=0.0, end_time=0.4, velocity=80, program=pg)
kira2_start.notes.add(pitch=74, start_time=0.4, end_time=0.6, velocity=80, program=pg)
kira2_start.notes.add(pitch=72, start_time=0.6, end_time=0.8, velocity=80, program=pg)
kira2_start.notes.add(pitch=69, start_time=0.8, end_time=1.2, velocity=80, program=pg)
kira2_start.notes.add(pitch=65, start_time=1.2, end_time=1.6, velocity=80, program=pg)
kira2_start.notes.add(pitch=67, start_time=1.6, end_time=2.2, velocity=80, program=pg)
kira2_start.notes.add(pitch=69, start_time=2.2, end_time=2.4, velocity=80, program=pg)
kira2_start.notes.add(pitch=67, start_time=2.4, end_time=3.2, velocity=80, program=pg)

kira2_start.notes.add(pitch=62, start_time=3.2, end_time=3.6, velocity=80, program=pg)
kira2_start.notes.add(pitch=65, start_time=3.6, end_time=3.8, velocity=80, program=pg)
kira2_start.notes.add(pitch=62, start_time=3.8, end_time=4.0, velocity=80, program=pg)
kira2_start.notes.add(pitch=60, start_time=4.0, end_time=4.4, velocity=80, program=pg)
kira2_start.notes.add(pitch=65, start_time=4.4, end_time=4.8, velocity=80, program=pg)
kira2_start.notes.add(pitch=69, start_time=4.8, end_time=5.2, velocity=80, program=pg)
kira2_start.notes.add(pitch=72, start_time=5.2, end_time=5.4, velocity=80, program=pg)
kira2_start.notes.add(pitch=69, start_time=5.4, end_time=5.6, velocity=80, program=pg)
kira2_start.notes.add(pitch=67, start_time=5.6, end_time=6.4, velocity=80, program=pg)



kira2_start.total_time = 6.4 
kira2_start.tempos.add(qpm=75);

note_seq.plot_sequence(kira2_start)
note_seq.play_sequence(kira2_start, synth=note_seq.fluidsynth)

# 最後のNoteSeqence
kira2_end = music_pb2.NoteSequence()
pg=18

kira2_end.notes.add(pitch=56, start_time=0.0, end_time=0.8, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=0.8, end_time=1.4, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=1.4, end_time=1.6, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=1.6, end_time=2.4, velocity=80, program=pg)
kira2_end.notes.add(pitch=59, start_time=2.4, end_time=3.0, velocity=80, program=pg)
kira2_end.notes.add(pitch=58, start_time=3.0, end_time=3.2, velocity=80, program=pg)

kira2_end.notes.add(pitch=58, start_time=3.2, end_time=3.8, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=3.8, end_time=4.0, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=4.0, end_time=4.6, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=4.6, end_time=4.8, velocity=80, program=pg)
kira2_end.notes.add(pitch=56, start_time=4.8, end_time=6.4, velocity=80, program=pg)


kira2_end.total_time = 6.4
kira2_end.tempos.add(qpm=75); 

note_seq.plot_sequence(kira2_end)
note_seq.play_sequence(kira2_end, synth=note_seq.fluidsynth)  # NoteSequenceの再生


kira2_mid = music_pb2.NoteSequence()
pg=11

kira2_mid.notes.add(pitch=60, start_time=0.0, end_time=0.13, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=0.13, end_time=0.26, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=0.26, end_time=0.4, velocity=80, program=pg)

kira2_mid.notes.add(pitch=60, start_time=0.4, end_time=1.6, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=1.6, end_time=1.73, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=1.73, end_time=1.86, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=1.86, end_time=2.0, velocity=80, program=pg)

kira2_mid.notes.add(pitch=60, start_time=2.0, end_time=2.8, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=2.8, end_time=2.93, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=2.93, end_time=3.06, velocity=80, program=pg)
kira2_mid.notes.add(pitch=60, start_time=3.06, end_time=3.2, velocity=80, program=pg)

kira2_mid.notes.add(pitch=64, start_time=3.2, end_time=3.6, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=3.6, end_time=3.73, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=3.73, end_time=3.86, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=3.86, end_time=4.0, velocity=80, program=pg)

kira2_mid.notes.add(pitch=64, start_time=4.0, end_time=4.4, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=4.4, end_time=4.53, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=4.53, end_time=4.66, velocity=80, program=pg)
kira2_mid.notes.add(pitch=64, start_time=4.66, end_time=4.8, velocity=80, program=pg)

kira2_mid.notes.add(pitch=67, start_time=4.8, end_time=5.2, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=5.2, end_time=5.33, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=5.33, end_time=5.46, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=5.46, end_time=5.6, velocity=80, program=pg)

kira2_mid.notes.add(pitch=67, start_time=5.6, end_time=6.0, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=6.0, end_time=6.13, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=6.13, end_time=6.26, velocity=80, program=pg)
kira2_mid.notes.add(pitch=67, start_time=6.26, end_time=6.4, velocity=80, program=pg)

kira2_mid.total_time = 6.4
kira2_mid.tempos.add(qpm=75); 

note_seq.plot_sequence(kira2_mid)
note_seq.play_sequence(kira2_mid, synth=note_seq.fluidsynth)  # NoteSequenceの再生

kira2_mid2 = music_pb2.NoteSequence()
pg=11

kira2_mid2.notes.add(pitch=72, start_time=0.0, end_time=0.8, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=71, start_time=0.8, end_time=1.4, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=66, start_time=1.4, end_time=1.6, velocity=80, program=pg)

kira2_mid2.notes.add(pitch=69, start_time=1.6, end_time=2.0, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=67, start_time=2.0, end_time=2.4, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=65, start_time=2.4, end_time=2.8, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=62, start_time=2.8, end_time=3.2, velocity=80, program=pg)

kira2_mid2.notes.add(pitch=60, start_time=3.2, end_time=4.0, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=62, start_time=4.0, end_time=4.4, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=57, start_time=4.4, end_time=4.67, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=62, start_time=4.67, end_time=4.8, velocity=80, program=pg)
kira2_mid2.notes.add(pitch=64, start_time=4.8, end_time=6.4, velocity=80, program=pg)

kira2_mid2.total_time = 6.4
kira2_mid2.tempos.add(qpm=75); 

note_seq.plot_sequence(kira2_mid2)
note_seq.play_sequence(kira2_mid2, synth=note_seq.fluidsynth)  # NoteSequenceの再生

n_seq = 4 # 曲のNoteSeqence数（最初と最後を含む）

# NoteSeqenceを複数生成し、リストに格納
gen_seq1 = music_vae.interpolate(
    kira2_start,  # 最初のNoteSeqence
    kira2_mid,  # 最後のNoteSeqence
    #kira2_end,
    num_steps=n_seq,
    length=32)

gen_seq2 = music_vae.interpolate(
    kira2_mid2,  # 最初のNoteSeqence
    kira2_end,  # 最後のNoteSeqence
    #kira2_end,
    num_steps=n_seq,
    length=32)



# NoteSeqenceを全て結合し、1つの曲に
interp_seq1 = note_seq.sequences_lib.concatenate_sequences(gen_seq1)

note_seq.plot_sequence(interp_seq1)
note_seq.play_sequence(interp_seq1, synth=note_seq.fluidsynth)

interp_seq2 = note_seq.sequences_lib.concatenate_sequences(gen_seq2)

note_seq.plot_sequence(interp_seq2)
note_seq.play_sequence(interp_seq2, synth=note_seq.fluidsynth)




     
