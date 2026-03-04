# /// script
# dependencies = [
#   "qrcode[pil]",
# ]
# ///
import qrcode

# 你提供的长链接
url = "https://webchannel-test.ciccwm.com/zzt/channel/kaihu-bytedance/index.html?acct_type=STOCK&broker_channel_code=DnRK2vz5ZH&douyin_channel_code=ad_kaihu&douyin_inner_channel_code=opentab4&expire_time=1773458802&param=BBoMzySxR%2FbKvjbLEJX7RdKgrOtZpkM5ceDDbLDsIgUnGY9hP4nDbdRlKrfriWT9al2RXi5S0%2BuwQrxFB8XDBT%2B7EvJkWh3pLL4%2BEhE0khiuswhelPAhMYdCQjFcwLpo3y4u7DYybZMB74dzgYaLi0xne4N2K3LP0D%2Bw6hF7bvhKuc66adu%2FmXr1cKm33Q5zbUo8jeZrhjleFd4ZTHwHBvzst8JzbBxoMr8opNnzPEMt9EVg95bnEOYDrJnE1tBzV0HExbPLQ885ivHLidwnpoDIn0N6LNUnbDFj55JscaUXFgHOFhzwi9%2FBl7Z9vykRF3MXTwZ3L6GmnlTivMYIumxYIMV%2FY0l9zyZPFn25sZVwEoU9YB152tU0NWR1HcMmkd0XiQJWJJkCPxNq1ExoiQz8PbvWV27dk7u4Th0g5qeT97%2BzGmpCyRlF4BbHEkFj6FCFWbQSRb%2FG2I8xt%2BBkPbcdPDKsUBKGTR45flfmTZxd0H05imSdM4QfIVtzyX1uxVACj%2FcuYJFxdJA3PdaGgixeNESpzTnsVhCyBZR0gd2HOVzL3XPvwDJO5DBxZZrYlHmmPmYWZLphJ2oHS%2FCarylc8c6aIRKG4nL4ZmkdurkOp0PHc2q%2BD5AVwdsCaaOYCE%2BijE7YTc5BxSQeai%2Fl7jQyQ6NMWiaNg0lYovfvvyuFYGVTpoqG%2B5Hffhf9Uj9k3wGFnPK7SPiSaQFRbu3YcsaYgEcx%2BAuo8hCp8RHodGZaEUa3iF86mb3eceeysEJZ%2FEqzaJMtzyTY485sBVdquIYV0xZ%2B88HipTVGHWD77etzoFxN%2Bq%2B9Ack3uP4jOOk1ULSdtdxGt972%2FBO4hMl4HkqCpVMX1lqCHY346YEiGZzPqaq5wI6x35axqEpSa4j6rhznJBf5GE93oVsNVF30y6b2RZ6jFcUG4hNDZ0OP3l7J%2FcLJoDZ9YdaFGKOhvF%2BhXO2fnDILUN3lryYjCuhA%2FLWg1tE2zUaJgrZp9bFqWiDbZeLHxtWe2dxHEIy%2FeY3vQHoSYCPzkaSfuig94C5t9uDaTuXQ6%2FEkWxWcq30r0xyeCu6G%2FQhdPg1QUosNibjFzMxXF9zt0qOeouw7n7IcOL4%3D&pass_through_info=%7B%22ADVERTISER_ID%22%3A%221759316927321102%22%2C%22CLICKID%22%3A%22B.eBa7IEwdefDUhKkmgOvZ5QFf4HxuSjeTA0ol6iN4LKtvBUPHAO4kywSVbUmLaYPIqQGHmIB3Xah2xyUwA8bYNTehg8JhBEJ7BvHfLXHe6gWcn8CMDyTzmdfPGffoMfzMBN%22%2C%22CTYPE%22%3A%2215%22%2C%22MID3%22%3A%227536077699226009646%22%2C%22PROJECT_ID%22%3A%227609637512625979398%22%2C%22PROMOTION_ID%22%3A%227609637585883381769%22%2C%22douyin_inner_channel_code%22%3A%22opentab4%22%2C%22envent_type%22%3A%22customer_effective%22%2C%22wp_args%22%3A%22%22%7D&trace_id=202603041126420627CtYSkwsdmHfMglxXP5rWS4IU5YXcB8tkeuFHdgIisk&noop=1"

# 配置二维码参数（因为链接比较长，稍微调整一下容错率）
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L, # 长链接用低容错即可，更容易扫出
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# 方式 1：打印在终端上（方便你直接掏出手机扫）
print("==== 终端扫码预览 ====")
qr.print_ascii(invert=True)
print("======================\n")

# 方式 2：生成对应的图片文件
img = qr.make_image(fill_color="black", back_color="white")
output_path = "qrcode.png"
img.save(output_path)
print(f"二维码图片已成功保存至当前目录下的: {output_path}")