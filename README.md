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


Home Assistant 用の SunSpec シミュレーター
この HACS コンポーネントは SunSpec の太陽光発電データをシミュレーション し、電力、電圧、状態を表示 します。
低電力の時に通知 を送信できます。ハードウェア不要、完全ソフトウェア実装！ 

インストール
1. HACS にカスタムリポジトリを追加： https://github.com/yinchak/home-assistant-sunspec-simulator  
2. 「Integration」 タイプを選択し、「SunSpec Simulator」を検索してインストール
3.  Home Assistant を再起動

使用方法
インストール後、以下のエンティティが利用可能になります：

sensor.sunspec_simulator_power （シミュレートされた電力）
sensor.sunspec_simulator_voltage （シミュレートされた電圧）
binary_sensor.sunspec_simulator_status （シミュレートされた状態）
30秒ごとにデータを更新 します！
電力が 100W 未満のとき、通知を送信（notify.mobile_app を設定する必要があります）

⚠ 注意事項
 -完全ソフトウェアシミュレーション（ESP32 や他のデバイスは不要）
 -実際の SunSpec デバイスがある場合は、接続を改善可能
