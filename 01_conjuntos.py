usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
assistiram = usuarios_data_science | usuarios_machine_learning
print(assistiram)
# set => conjunto => Exemplo: {1, 2, 3}
# print(set(assistiram))
assistiram2 = usuarios_data_science & usuarios_machine_learning
print(assistiram2)
assistiram3 = usuarios_data_science - usuarios_machine_learning
print(assistiram3)
assistiram4 = usuarios_data_science ^ usuarios_machine_learning
print(assistiram4)