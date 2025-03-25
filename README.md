# SunSpec Simulator for Home Assistant

呢個HACS組件模擬SunSpec太陽能數據，展示功率、電壓同狀態，喺低功率時發通知。唔使任何硬件，純軟件實現。

## 安裝
1. 喺HACS加自訂倉庫：`https://github.com/yinchak/home-assistant-sunspec-simulator`
2. 類型選「Integration」，搜尋「SunSpec Simulator」並安裝。
3. 重啟Home Assistant。

## 使用
- 安裝後，會有以下實體：
  - `sensor.sunspec_simulator_power`（模擬功率）
  - `sensor.sunspec_simulator_voltage`（模擬電壓）
  - `binary_sensor.sunspec_simulator_status`（模擬狀態）
- 每30秒更新一次數據。
- 功率低於100W時發通知（要設好`notify.mobile_app`）。

## 注意
- 純軟件模擬，唔使ESP32或其他設備。
- 有真SunSpec設備時可改進連繫。