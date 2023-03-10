import streamlit as st
import magenta
import note_seq
from note_seq.protobuf import music_pb2

kira2 = music_pb2.NoteSequence()  # NoteSequence

pg = 12  # 楽器の種類 -ここを変更-
is_dm = False  # ドラムかどうか -ここを変更-

# notesにnoteを追加
kira2.notes.add(pitch=60, start_time=0.0, end_time=0.4, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=60, start_time=0.4, end_time=0.8, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=67, start_time=0.8, end_time=1.2, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=67, start_time=1.2, end_time=1.6, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=69, start_time=1.6, end_time=2.0, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=69, start_time=2.0, end_time=2.4, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=67, start_time=2.4, end_time=3.2, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=65, start_time=3.2, end_time=3.6, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=65, start_time=3.6, end_time=4.0, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=64, start_time=4.0, end_time=4.4, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=64, start_time=4.4, end_time=4.8, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=62, start_time=4.8, end_time=5.2, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=62, start_time=5.2, end_time=5.6, velocity=80, program=pg, is_drum=is_dm)
kira2.notes.add(pitch=60, start_time=5.6, end_time=6.4, velocity=80, program=pg, is_drum=is_dm) 

note_seq.plot_sequence(kira2)  # NoteSequenceの可視化
note_seq.play_sequence(kira2, synth=note_seq.fluidsynth)  # NoteSequenceの再生
