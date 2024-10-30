import nest

# 시뮬레이션 커널 초기화
nest.ResetKernel()

# 신경 세포 생성
neurons = nest.Create("iaf_neuron", 10)  # 10개의 신경세포 생성
stimulus = nest.Create("dc_generator", 1)  # DC 전류 생성기 생성

# 생성한 신경세포에 자극 연결
nest.Connect(stimulus, neurons)

# 신경세포 상태 설정
nest.SetStatus(stimulus, {"amplitude": 1.0, "start": 100.0, "stop": 900.0})

# 시뮬레이션 실행
nest.Simulate(1000.0)  # 1000 ms 동안 시뮬레이션

# 결과 플로팅
nest.raster_plot()
