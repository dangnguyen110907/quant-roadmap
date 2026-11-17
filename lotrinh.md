# LỘ TRÌNH QUANT VÀ DATA SCIENCE (69 BƯỚC CHUẨN)

Nguồn gốc: https://dsroadmap-five.vercel.app/
Tệp này là căn cứ duy nhất để xác định nội dung học, bài tập, bài lab và tiêu chí nghiệm thu Cổng kiểm tra.


## Giai đoạn 1: Công cụ và Python (tuần 1–4)

### Bước 01: Terminal và shell
- **Mục tiêu:** Dùng terminal thoải mái, viết được script ngắn
- **Học:** Missing Semester (MIT): bài Course overview + Shell, và bài Shell Tools and Scripting. Gõ lại từng lệnh.
- **Bài tập:** Làm bài tập cuối hai bài trên; ghi mỗi lệnh mới vào cheatsheet.md.
- **Bài code:** Cài Miniconda, tạo môi trường quant, viết script shell đếm dòng lỗi trong file log bằng grep | sort | uniq -c.
- **Lab:** Chạy được conda activate rồi python --version.
- **Cổng kiểm tra:** Tự gõ pipeline lọc và đếm dữ liệu mà không tra lại.
- **Không cần học:** Vim nâng cao, tuỳ biến zsh, Docker.

### Bước 02: Git và GitHub
- **Mục tiêu:** Làm việc với branch, conflict, pull request
- **Học:** Missing Semester: bài Version Control (Git). Pro Git chương 2 và 3.
- **Bài tập:** Làm bài tập cuối bài Version Control; luyện trên learngitbranching.js.org.
- **Bài code:** Tạo repo quant-roadmap trên GitHub: .gitignore cho Python, 3 branch, 1 pull request.
- **Lab:** Tự gây conflict giữa hai branch rồi giải quyết.
- **Cổng kiểm tra:** Gây và giải quyết conflict mà không xem hướng dẫn.
- **Không cần học:** Git internals, submodule, hooks.

### Bước 03: Python cơ bản
- **Mục tiêu:** Viết hàm sạch, đọc ghi file, bắt lỗi
- **Học:** CS50P (Harvard): bài giảng 0 đến 4 (functions, conditionals, loops, exceptions, libraries).
- **Bài tập:** Làm Problem Set của từng bài, tự chạy thử để kiểm tra.
- **Bài code:** Đọc CSV giá cổ phiếu, ghi ra JSON, bắt lỗi file thiếu và dòng hỏng.
- **Lab:** Viết lại cùng chương trình theo hướng chia nhỏ thành 3 hàm.
- **Cổng kiểm tra:** Giải bài tương tự chưa thấy trong 30 phút.
- **Không cần học:** Regex, web framework.

### Bước 04: Python chuyên sâu và Project 1
- **Mục tiêu:** Có test, có cấu trúc, có OOP cơ bản
- **Học:** CS50P bài 5 (unit tests), 6 (file I/O), 8 (OOP). Tự tra dataclass, generator, decorator trong tài liệu Python chính thức.
- **Bài tập:** Problem Set bài 5, 6, 8; viết pytest cho 3 hàm đã có.
- **Bài code:** Project 1: mô phỏng Tài Xỉu 100.000 ván, nhà cái ăn 3%, vẽ đường vốn của 100 người chơi.
- **Lab:** Chia hàm sạch, có pytest, có README.
- **Cổng kiểm tra:** Project 1 đạt 7 tiêu chuẩn hoàn thành một project (README, chạy lại được, baseline, hạn chế, biểu đồ...).
- **Không cần học:** asyncio, metaclass, C++.


## Giai đoạn 2: Dữ liệu và SQL (tuần 5–12)

### Bước 05: NumPy và pandas cơ bản
- **Mục tiêu:** Xử lý bảng dữ liệu không dùng vòng for
- **Học:** Python for Data Analysis (McKinney) chương 4, 5 và 7.
- **Bài tập:** Làm lại ví dụ trong chương trên bằng dữ liệu của riêng bạn, không chép nguyên.
- **Bài code:** Tải CSV giá BTC 1 năm; làm sạch thiếu, trùng, sai kiểu; viết hàm báo cáo chất lượng dữ liệu.
- **Lab:** Thay mọi vòng for trên DataFrame bằng vectorization và đo thời gian.
- **Cổng kiểm tra:** Giải thích vì sao for loop trên DataFrame chậm và chứng minh bằng số đo.
- **Không cần học:** Polars, DuckDB, Spark.

### Bước 06: pandas chuỗi thời gian và Project 2
- **Mục tiêu:** Tính lợi suất, biến động, tương quan
- **Học:** McKinney chương 8, 10, 11 (ghép bảng, groupby, time series).
- **Bài tập:** Bài tập resample, rolling, shift, pct_change, merge_asof trên dữ liệu BTC và ETH.
- **Bài code:** Project 2: lợi suất ngày, volatility 30 ngày, tương quan BTC với ETH, biểu đồ.
- **Lab:** Kiểm tra timestamp lệch giữa hai nguồn bằng merge_asof.
- **Cổng kiểm tra:** Project 2 đạt 7 tiêu chuẩn hoàn thành một project.
- **Không cần học:** Polars, DuckDB, phân trang API nâng cao.

### Bước 07: SQL nền
- **Mục tiêu:** JOIN, GROUP BY, subquery thành thạo
- **Học:** SQLBolt: toàn bộ phần truy vấn và JOIN.
- **Bài tập:** LeetCode SQL 50: hết nhóm Easy, bắt đầu Medium, 3 bài mỗi ngày.
- **Bài code:** Cài SQLite, nạp CSV giá nến vào bảng, viết truy vấn JOIN và GROUP BY.
- **Lab:** Viết lại 5 phép tính pandas thành SQL và so kết quả.
- **Cổng kiểm tra:** Giải bài JOIN và subquery Medium chưa thấy trong 20 phút.
- **Không cần học:** Stored procedure, tối ưu index sâu.

### Bước 08: SQL window và Project 3
- **Mục tiêu:** Window function và CSDL giá nến
- **Học:** Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER, ROWS BETWEEN) trong tài liệu PostgreSQL. Use The Index, Luke: chỉ đọc phần giới thiệu.
- **Bài tập:** LeetCode SQL 50: các bài Medium dùng window function.
- **Bài code:** Project 3: CSDL SQLite hoặc PostgreSQL nhiều mã, truy vấn lợi suất theo tuần và xếp hạng biến động.
- **Lab:** Chạy EXPLAIN trước và sau khi thêm index.
- **Cổng kiểm tra:** Project 3 đạt 7 tiêu chuẩn hoàn thành một project.
- **Không cần học:** Power BI, Excel (xếp ở giai đoạn 4), NoSQL.

### Bước 09: Dữ liệu thị trường: ccxt, vnstock, API
- **Mục tiêu:** Tự kéo dữ liệu crypto và chứng khoán VN ổn định
- **Học:** Tài liệu ccxt (dữ liệu nến, giới hạn truy cập) và vnstock (vnstocks.com; cần đăng ký API key miễn phí, API đã đổi nhiều lần nên làm theo tài liệu bản mới nhất); McKinney chương 6 (nạp dữ liệu).
- **Bài tập:** Viết hàm gọi API có phân trang, thử lại khi lỗi, không để API key trong code (dùng biến môi trường).
- **Bài code:** Kéo 5 mã crypto và 5 mã VN30, lưu thành parquet hoặc SQLite theo ngày.
- **Lab:** Chạy lại script sau 1 ngày, kiểm tra dữ liệu mới nối đúng và không trùng.
- **Cổng kiểm tra:** Script tự cập nhật dữ liệu, không lỗi trong 3 lần chạy liên tiếp.
- **Không cần học:** Websocket, dữ liệu tick.

### Bước 10: Polars, DuckDB và kiểm tra chất lượng dữ liệu
- **Mục tiêu:** Xử lý dữ liệu lớn nhanh và đáng tin
- **Học:** Polars User Guide (phần lazy) và tài liệu DuckDB (đọc parquet bằng SQL).
- **Bài tập:** Viết lại 5 phép tính của tuần 7: 5 bằng Polars, 5 bằng DuckDB.
- **Bài code:** Truy vấn file parquet của tuần 9 bằng DuckDB, so thời gian với pandas.
- **Lab:** Viết hàm kiểm tra chất lượng: thiếu, trùng, timestamp lệch, giá bất thường.
- **Cổng kiểm tra:** Giải thích một lỗi dữ liệu và cách phân biệt nó với biến động thật.
- **Không cần học:** Spark, Hadoop.

### Bước 11: Backtest đầu tay (cố tình sai)
- **Mục tiêu:** Chạm sớm vào thứ bạn muốn làm và thấy lỗi nằm ở đâu
- **Học:** backtesting.py hoặc vectorbt: chỉ đọc quickstart. Không cần lý thuyết mới.
- **Bài tập:** Viết trên giấy quy tắc cắt chéo MA và đoán trước kết quả hơn hay kém buy-and-hold.
- **Bài code:** Backtest cắt chéo MA 20/50 cho BTC bằng pandas; lần 1 cố tình dùng tín hiệu cùng ngày (look-ahead), lần 2 shift 1 kỳ.
- **Lab:** Đo chênh lệch đường vốn của hai lần chạy và so với buy-and-hold.
- **Cổng kiểm tra:** Giải thích bằng số vì sao lần 1 đẹp hơn mà vô giá trị.
- **Không cần học:** Tối ưu tham số, thư viện nâng cao. Sẽ học lại đúng cách ở giai đoạn 5.

### Bước 12: Tuần đệm (làm bù, không học mới)
- **Mục tiêu:** Bù ô còn trống và củng cố chỗ yếu
- **Học:** Xem lại danh sách lỗi đã ghi và chọn 3 chủ đề còn yếu nhất.
- **Bài tập:** Làm lại các bài đã sai hoặc bỏ dở.
- **Bài code:** Dọn code, commit các project đang dở, cập nhật README.
- **Lab:** Chạy lại mọi notebook từ đầu để chắc chắn chạy được.
- **Cổng kiểm tra:** Mọi ô của các tuần trước đã tick, hoặc đã ghi lý do bỏ.
- **Không cần học:** Học nội dung mới.


## Giai đoạn 3: Toán nền: xác suất, thống kê, đại số, tối ưu (tuần 13–29)

### Bước 13: Xác suất 1: đếm và có điều kiện
- **Mục tiêu:** Nắm Bayes và xác suất có điều kiện
- **Học:** Stat 110 (Harvard) Lecture 1 đến 5. Đối chiếu mục lục trên trang khoá học.
- **Bài tập:** Bài tập trong Introduction to Probability (Blitzstein và Hwang), chọn khoảng một nửa số bài (ưu tiên bài có lời giải); kẹt quá 30 phút thì xem lời giải rồi tự làm lại.
- **Bài code:** Mô phỏng Python: bài sinh nhật, Monty Hall, Bayes cho xét nghiệm bệnh hiếm.
- **Lab:** Mỗi đáp án lý thuyết phải đối chiếu với mô phỏng.
- **Cổng kiểm tra:** Tự giải 5 bài xác suất có điều kiện chưa thấy.
- **Không cần học:** Story proof dài, tổ hợp nâng cao.

### Bước 14: Xác suất 2: kỳ vọng và Gambler’s Ruin
- **Mục tiêu:** Tính kỳ vọng và xác suất phá sản
- **Học:** Stat 110 Lecture 6 đến 10 (biến ngẫu nhiên, Gambler’s Ruin, kỳ vọng, tuyến tính của kỳ vọng).
- **Bài tập:** Bài tập kỳ vọng và indicator trong sách đi kèm.
- **Bài code:** Mô phỏng Gambler’s Ruin với nhiều mức vốn và xác suất thắng.
- **Lab:** Đối chiếu công thức với mô phỏng.
- **Cổng kiểm tra:** Tính xác suất cháy tài khoản bằng công thức rồi đối chiếu mô phỏng Python.
- **Không cần học:** Martingale chính quy.

### Bước 15: Xác suất 3: phân phối
- **Mục tiêu:** Dùng đúng Nhị thức, Poisson, Chuẩn
- **Học:** Stat 110 Lecture 11 đến 15 (Nhị thức, Poisson, Chuẩn). Đối chiếu mục lục.
- **Bài tập:** Bài tập phân phối trong sách đi kèm.
- **Bài code:** Vẽ phân phối lý thuyết đè lên histogram lợi suất BTC.
- **Lab:** Kiểm tra lợi suất BTC có giống phân phối Chuẩn không.
- **Cổng kiểm tra:** Giải thích bằng số liệu vì sao lợi suất tài chính có đuôi dày.
- **Không cần học:** Hàm sinh moment.

### Bước 16: Xác suất 3b: biến ngẫu nhiên nhiều chiều, hiệp phương sai
- **Mục tiêu:** Hiểu hiệp phương sai, tương quan, kỳ vọng có điều kiện (nền cho PCA, Markowitz)
- **Học:** Stat 110: các bài về phân phối đồng thời, hiệp phương sai, tương quan, kỳ vọng có điều kiện (tra mục lục khoá học).
- **Bài tập:** Bài tập phân phối đồng thời và hiệp phương sai trong sách Blitzstein; tự chứng minh Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y).
- **Bài code:** Mô phỏng hai biến chuẩn tương quan; tính ma trận hiệp phương sai lợi suất BTC, ETH và so với np.cov.
- **Lab:** Vẽ scatter ở rho = 0, 0.5, -0.9 và đối chiếu hệ số tương quan mẫu.
- **Cổng kiểm tra:** Tính tay phương sai của danh mục hai tài sản rồi đối chiếu bằng mô phỏng.
- **Không cần học:** Chuẩn nhiều chiều tổng quát, copula.

### Bước 17: Xác suất 4: LLN và CLT
- **Mục tiêu:** Hiểu vì sao trung bình mẫu ổn định
- **Học:** Stat 110: các bài về Luật số lớn và Định lý Giới hạn Trung tâm (tra mục lục khoá học).
- **Bài tập:** Bài tập LLN, CLT trong sách đi kèm.
- **Bài code:** Mô phỏng CLT bằng tổng nhiều phân phối khác nhau.
- **Lab:** Đo tốc độ hội tụ khi tăng cỡ mẫu.
- **Cổng kiểm tra:** Giải thích CLT cho người không chuyên trong 3 phút.
- **Không cần học:** Chứng minh CLT bằng hàm đặc trưng.

### Bước 18: Xác suất 5: Markov chain và bài toán đếm
- **Mục tiêu:** Giải được bài đếm và Markov chain hay gặp khi phỏng vấn
- **Học:** Stat 110: các bài về Markov chain (tra mục lục khoá học). Green Book: phần xác suất.
- **Bài tập:** Giải tay 10 bài đếm (hoán vị, tổ hợp) và 5 bài Markov chain trong sách Blitzstein.
- **Bài code:** Mô phỏng Markov chain 3 trạng thái (thị trường tăng, giảm, đi ngang), tìm phân phối dừng bằng lũy thừa ma trận.
- **Lab:** So phân phối dừng tính bằng trị riêng (numpy.linalg.eig) với kết quả mô phỏng.
- **Cổng kiểm tra:** Tự giải 5 bài đếm và 3 bài Markov chưa thấy.
- **Không cần học:** Markov chain liên tục, martingale chính quy.

### Bước 19: Thống kê 1: kiểm định giả thuyết, p-value
- **Mục tiêu:** Hiểu đúng p-value và sai số loại I, II
- **Học:** ISLP chương 13 (phần kiểm định giả thuyết). StatQuest: p-value, t-test.
- **Bài tập:** Bài tập chương 13 về sai số loại I và II; tự tính p-value của kiểm định t bằng tay.
- **Bài code:** Dùng scipy.stats chạy t-test cho lợi suất BTC ở hai giai đoạn, rồi tự viết lại t-test bằng NumPy và đối chiếu.
- **Lab:** Mô phỏng 10.000 kiểm định khi giả thuyết không đúng: tỷ lệ p<0.05 phải xấp xỉ 5%.
- **Cổng kiểm tra:** Giải thích p-value cho người không học thống kê trong 2 phút, nêu 2 cách hiểu sai phổ biến.
- **Không cần học:** Kiểm định phi tham số chuyên sâu, thống kê Bayes.

### Bước 20: Thống kê 2: hồi quy OLS và chẩn đoán
- **Mục tiêu:** Dùng OLS và biết khi nào kết quả không đáng tin
- **Học:** ISLP chương 3 (hồi quy tuyến tính). StatQuest: linear regression, R-squared.
- **Bài tập:** Bài tập chương 3; suy ra công thức OLS β=(X'X)^-1 X'y bằng tay.
- **Bài code:** Fit OLS bằng statsmodels hồi quy lợi suất ETH theo BTC, vẽ phần dư; tự viết OLS bằng NumPy và so hệ số.
- **Lab:** Kiểm tra giả định: phần dư, phương sai không đồng nhất (Breusch-Pagan), đa cộng tuyến (VIF).
- **Cổng kiểm tra:** Chỉ ra giả định nào bị vi phạm trong dữ liệu của bạn và hậu quả với kết luận.
- **Không cần học:** Hồi quy phi tuyến, mô hình hỗn hợp.

### Bước 21: Thống kê 3: bootstrap, permutation, multiple testing
- **Mục tiêu:** Nhận ra “lãi ảo” do may mắn
- **Học:** ISLP chương 5 (bootstrap) và chương 13 (Bonferroni, FDR).
- **Bài tập:** Bài tập chương 5 và 13; tự tính FDR (Benjamini-Hochberg) bằng tay cho 10 giá trị p.
- **Bài code:** Mô phỏng 100 chiến lược giao dịch ngẫu nhiên, đếm số chiến lược “lãi ảo”, lọc bằng Bonferroni và FDR.
- **Lab:** Dùng bootstrap tính khoảng tin cậy của Sharpe; dùng permutation test so hai chiến lược.
- **Cổng kiểm tra:** Chứng minh bằng mô phỏng rằng thử nhiều chiến lược thì chắc chắn có vài cái lãi vì may mắn.
- **Không cần học:** Thiết kế thí nghiệm nâng cao.

### Bước 22: Thống kê 4: logistic, MLE, A/B testing
- **Mục tiêu:** Nền của credit scoring và thí nghiệm A/B
- **Học:** ISLP chương 4 (logistic). Evan Miller: công cụ tính cỡ mẫu A/B. StatQuest: MLE.
- **Bài tập:** Suy ra log-likelihood của logistic bằng tay; tính cỡ mẫu A/B cho tỷ lệ chuyển đổi từ 5% lên 6%.
- **Bài code:** Fit logistic bằng statsmodels dự đoán lợi suất ngày mai dương hay âm; viết hàm mô phỏng A/B test.
- **Lab:** Mô phỏng lỗi “nhìn kết quả giữa chừng” và đo tỷ lệ dương tính giả.
- **Cổng kiểm tra:** Tính cỡ mẫu và power cho một A/B test chưa thấy và giải thích từng tham số.
- **Không cần học:** Bayesian A/B, multi-armed bandit.

### Bước 23: Tuần đệm (làm bù, không học mới)
- **Mục tiêu:** Bù ô còn trống và củng cố chỗ yếu
- **Học:** Xem lại danh sách lỗi đã ghi và chọn 3 chủ đề còn yếu nhất.
- **Bài tập:** Làm lại các bài đã sai hoặc bỏ dở.
- **Bài code:** Dọn code, commit các project đang dở, cập nhật README.
- **Lab:** Chạy lại mọi notebook từ đầu để chắc chắn chạy được.
- **Cổng kiểm tra:** Mọi ô của các tuần trước đã tick, hoặc đã ghi lý do bỏ.
- **Không cần học:** Học nội dung mới.

### Bước 24: Đại số tuyến tính 1
- **Mục tiêu:** Nắm trị riêng, vector riêng bằng hình học và phép tính
- **Học:** 3Blue1Brown: Essence of Linear Algebra (toàn bộ). MIT 18.06 (Strang): các bài đầu về hệ phương trình, phép khử, ma trận.
- **Bài tập:** Giải tay hệ phương trình bằng phép khử; tích ma trận; trị riêng của ma trận 2x2 và 3x3.
- **Bài code:** Dùng numpy.linalg giải hệ, tính trị riêng, vector riêng; kiểm tra Av = λv.
- **Lab:** Viết lại phép khử Gauss bằng Python thuần và so với numpy.linalg.solve.
- **Cổng kiểm tra:** Giải thích bằng hình học trị riêng và vector riêng là gì, không dùng công thức.
- **Không cần học:** Không gian vector trừu tượng, dạng Jordan.

### Bước 25: Đại số tuyến tính 2: SVD, PCA
- **Mục tiêu:** Rút gọn chiều dữ liệu bằng SVD và PCA
- **Học:** MIT 18.06: bài về SVD và phép chiếu. ISLP chương 12 (PCA).
- **Bài tập:** Tính SVD tay cho ma trận 2x2; chứng minh PCA là phân tích trị riêng của ma trận hiệp phương sai.
- **Bài code:** Chạy PCA lên lợi suất 10 mã VN30, vẽ phương sai giải thích theo số thành phần; tự viết PCA bằng SVD.
- **Lab:** So kết quả PCA tự viết với sklearn.decomposition.PCA.
- **Cổng kiểm tra:** Giải thích vì sao thành phần chính đầu của lợi suất cổ phiếu thường là “thị trường chung”.
- **Không cần học:** Kernel PCA, tensor.

### Bước 26: Ledoit-Wolf, ma trận xác định dương
- **Mục tiêu:** Hiểu vì sao ma trận hiệp phương sai mẫu gây nhiễu
- **Học:** Tài liệu scikit-learn về LedoitWolf (covariance estimation). MIT 18.06: bài về ma trận xác định dương.
- **Bài tập:** Chứng minh ma trận hiệp phương sai mẫu là nửa xác định dương; giải thích vì sao nhiễu lớn khi số mã gần bằng số quan sát.
- **Bài code:** So ma trận hiệp phương sai mẫu và Ledoit-Wolf trên 30 mã VN30 với 60 ngày dữ liệu.
- **Lab:** Đo số điều kiện (condition number) của hai ma trận.
- **Cổng kiểm tra:** Giải thích bằng ví dụ số vì sao ma trận mẫu làm danh mục tối ưu bất ổn.
- **Không cần học:** Random Matrix Theory.

### Bước 27: Giải tích nhiều biến, nhân tử Lagrange
- **Mục tiêu:** Tối ưu có ràng buộc bằng tay và bằng code
- **Học:** 3Blue1Brown: Essence of Calculus. Boyd, Convex Optimization: chương 1–2 (giới thiệu, tập lồi).
- **Bài tập:** Tính gradient và Hessian tay cho 5 hàm nhiều biến; giải 3 bài tối ưu có ràng buộc bằng Lagrange.
- **Bài code:** Dùng scipy.optimize.minimize tối ưu danh mục 3 mã với tổng tỷ trọng bằng 1; đối chiếu với nghiệm Lagrange tính tay.
- **Lab:** Vẽ đường đồng mức và gradient của một hàm hai biến.
- **Cổng kiểm tra:** Giải bài tối ưu có ràng buộc chưa thấy bằng Lagrange trong 20 phút.
- **Không cần học:** Điều kiện KKT chi tiết, tối ưu phi lồi.

### Bước 28: Gradient Descent tự viết
- **Mục tiêu:** Hiểu thuật toán nằm dưới mọi mô hình ML
- **Học:** Andrew Ng, Machine Learning Specialization: phần gradient descent cho hồi quy tuyến tính. Boyd chương 9: chỉ đọc phần giới thiệu.
- **Bài tập:** Suy ra đạo hàm hàm mất mát MSE bằng tay; giải thích learning rate quá lớn và quá nhỏ.
- **Bài code:** Tự viết gradient descent cho hồi quy tuyến tính bằng NumPy, thêm momentum, vẽ đường hội tụ.
- **Lab:** So kết quả với nghiệm OLS của tuần 20.
- **Cổng kiểm tra:** Viết lại gradient descent từ đầu không xem lại, kết quả khớp OLS đến 4 chữ số thập phân.
- **Không cần học:** Adam, tối ưu bậc hai.

### Bước 29: Tuần đệm (làm bù, không học mới)
- **Mục tiêu:** Bù ô còn trống và củng cố chỗ yếu
- **Học:** Xem lại danh sách lỗi đã ghi và chọn 3 chủ đề còn yếu nhất.
- **Bài tập:** Làm lại các bài đã sai hoặc bỏ dở.
- **Bài code:** Dọn code, commit các project đang dở, cập nhật README.
- **Lab:** Chạy lại mọi notebook từ đầu để chắc chắn chạy được.
- **Cổng kiểm tra:** Mọi ô của các tuần trước đã tick, hoặc đã ghi lý do bỏ.
- **Không cần học:** Học nội dung mới.


## Giai đoạn 4: ML và chuỗi thời gian (tuần 30–43)

### Bước 30: ML nền: train/val/test, cross-validation
- **Mục tiêu:** Chia dữ liệu và đánh giá đúng
- **Học:** ISLP chương 5 (resampling). Andrew Ng, ML Specialization: khóa 1 (hồi quy, phân loại); khóa 2 chỉ xem phần cây quyết định, bỏ neural network.
- **Bài tập:** Bài tập chương 5; tính tay k-fold cho 10 điểm.
- **Bài code:** Pipeline scikit-learn: chia train/val/test, k-fold, so 3 mô hình trên dữ liệu BTC.
- **Lab:** Vẽ đường học (learning curve) cho bias-variance.
- **Cổng kiểm tra:** Giải thích bias-variance bằng đồ thị của chính bạn.
- **Không cần học:** Neural network sâu.

### Bước 31: Regularization, cây quyết định, Random Forest
- **Mục tiêu:** Chống overfit bằng phạt và cây
- **Học:** ISLP chương 6 (Ridge, Lasso) và chương 8 (cây, Random Forest).
- **Bài tập:** Bài tập chương 6 và 8; tính tay Gini cho một lần tách cây.
- **Bài code:** Ridge/Lasso và Random Forest trên dữ liệu giá; so với hồi quy thường.
- **Lab:** Chọn alpha bằng cross-validation.
- **Cổng kiểm tra:** Giải thích vì sao Lasso đưa hệ số về 0 còn Ridge thì không.
- **Không cần học:** SVM, neural network.

### Bước 32: XGBoost/LightGBM, feature engineering
- **Mục tiêu:** Mô hình mạnh nhất cho dữ liệu bảng
- **Học:** Tài liệu XGBoost và LightGBM (Getting Started); ISLP chương 8 phần boosting.
- **Bài tập:** Giải thích gradient boosting bằng lời và vẽ 3 bước lặp.
- **Bài code:** Train XGBoost dự đoán hướng giá, tinh chỉnh tham số có kiểm soát.
- **Lab:** Tạo 10 đặc trưng từ giá (động lượng, biến động) và đo độ quan trọng.
- **Cổng kiểm tra:** Nêu số liệu: mô hình có thắng baseline đơn giản ngoài mẫu không.
- **Không cần học:** Bayesian optimization.

### Bước 33: Chống look-ahead và leakage, Purged CV
- **Mục tiêu:** Không để dữ liệu tương lai rò vào huấn luyện
- **Học:** López de Prado, Advances in Financial ML: chương cross-validation trong tài chính (Purged, Embargo). Sách khó: đọc để hiểu ý tưởng, không cần tái hiện từng dòng code.
- **Bài tập:** Vẽ sơ đồ k-fold thường và Purged k-fold trên trục thời gian.
- **Bài code:** Cài hàm Purged K-Fold có embargo và so điểm với k-fold thường.
- **Lab:** Cố ý tạo leakage (dùng giá ngày mai) và đo mức điểm ảo.
- **Cổng kiểm tra:** Chỉ ra 3 nguồn look-ahead bias trong pipeline của bạn.
- **Không cần học:** Combinatorial Purged CV.

### Bước 34: Triple Barrier, gán nhãn
- **Mục tiêu:** Gán nhãn theo chốt lời, cắt lỗ
- **Học:** López de Prado: chương gán nhãn (Triple Barrier, meta-labeling).
- **Bài tập:** Tính tay nhãn cho 5 điểm với chốt lời, cắt lỗ, giới hạn thời gian.
- **Bài code:** Cài Triple Barrier bằng pandas, huấn luyện mô hình trên nhãn mới.
- **Lab:** So kết quả với nhãn cố định theo ngày.
- **Cổng kiểm tra:** Giải thích vì sao nhãn theo ngày cố định gây sai lệch.
- **Không cần học:** Fractional differentiation.

### Bước 35: Phân loại thực tế: mất cân bằng, ROC/PR-AUC, SHAP
- **Mục tiêu:** Đánh giá và giải thích mô hình phân loại
- **Học:** Tài liệu scikit-learn: metrics, class_weight, calibration; tài liệu SHAP.
- **Bài tập:** Tính tay precision, recall, ROC-AUC cho bảng nhầm lẫn nhỏ.
- **Bài code:** Dữ liệu mất cân bằng: class_weight, chọn ngưỡng, PR-AUC, giải thích bằng SHAP.
- **Lab:** Phân tích 20 dự đoán sai nhiều nhất.
- **Cổng kiểm tra:** Chọn ngưỡng cắt và giải thích đánh đổi bằng số liệu.
- **Không cần học:** Deep learning cho dữ liệu bảng.

### Bước 36: Chuỗi thời gian 1: tính dừng, ADF, ACF/PACF
- **Mục tiêu:** Biết chuỗi nào dừng, chuỗi nào không
- **Học:** Hyndman FPP3: chương tính dừng và ACF (sách viết bằng R: đọc lý thuyết, tự làm bằng Python); statsmodels: adfuller.
- **Bài tập:** Làm toán AR(1), MA(1): tính ACF lý thuyết.
- **Bài code:** ADF test và ACF/PACF cho giá và lợi suất log của BTC.
- **Lab:** Biến đổi giá thành chuỗi dừng bằng sai phân.
- **Cổng kiểm tra:** Phân biệt giá (không dừng) và lợi suất (dừng) bằng số liệu.
- **Không cần học:** Kalman filter.

### Bước 37: Chuỗi thời gian 2: ARIMA và dự báo
- **Mục tiêu:** Dự báo và so với baseline
- **Học:** Hyndman FPP3: chương ARIMA; statsmodels: ARIMA.
- **Bài tập:** Chọn bậc (p,d,q) bằng tay từ ACF/PACF.
- **Bài code:** Fit ARIMA, dự báo 30 ngày, so với baseline naive.
- **Lab:** Kiểm tra phần dư bằng Ljung-Box.
- **Cổng kiểm tra:** Chứng minh mô hình có thắng baseline naive ngoài mẫu hay không.
- **Không cần học:** SARIMA, VAR.

### Bước 38: GARCH và volatility
- **Mục tiêu:** Dự báo biến động giá
- **Học:** Tài liệu arch (ví dụ GARCH); Ruppert, Statistics and Data Analysis for Financial Engineering: chương GARCH.
- **Bài tập:** Giải thích volatility clustering và công thức GARCH(1,1).
- **Bài code:** Fit GARCH(1,1) cho lợi suất BTC, dự báo biến động ngày mai.
- **Lab:** So với độ lệch chuẩn trượt 30 ngày.
- **Cổng kiểm tra:** Đánh giá dự báo biến động ngoài mẫu bằng sai số cụ thể.
- **Không cần học:** EGARCH, GJR.

### Bước 39: Walk-forward, đánh giá ngoài mẫu
- **Mục tiêu:** Đánh giá đúng cho chuỗi thời gian
- **Học:** Hyndman FPP3: đánh giá dự báo, cross-validation chuỗi thời gian.
- **Bài tập:** Thiết kế cửa sổ walk-forward trên giấy.
- **Bài code:** Cài walk-forward cho mô hình của tuần 32 và 38.
- **Lab:** So walk-forward với k-fold thường.
- **Cổng kiểm tra:** Giải thích vì sao k-fold thường sai với chuỗi thời gian.
- **Không cần học:** Online learning.

### Bước 40: Scorecard tín dụng: WoE, IV, KS, PSI
- **Mục tiêu:** Làm credit scoring đúng kiểu ngân hàng
- **Học:** ISLP chương 4 (logistic). Tài liệu optbinning và bài viết về scorecard: binning, WoE, IV.
- **Bài tập:** Tính tay WoE và IV cho một biến 4 nhóm; giải thích vì sao IV quá cao là dấu hiệu leakage.
- **Bài code:** Binning 3 biến, tính WoE/IV, fit logistic trên biến WoE, tính KS và Gini.
- **Lab:** Tính PSI giữa tập train và tập test, giải thích ngưỡng.
- **Cổng kiểm tra:** Giải thích cho người không chuyên: WoE, KS, PSI cho biết điều gì về mô hình.
- **Không cần học:** Reject inference, Basel chi tiết.

### Bước 41: Project 5 (phần 1): credit scoring hoặc fraud
- **Mục tiêu:** Dựng baseline cho đường lui ngân hàng
- **Học:** ISLP chương 4; scikit-learn: xử lý mất cân bằng.
- **Bài tập:** Lập kế hoạch Project 5: bài toán, dữ liệu Kaggle, chỉ số, baseline.
- **Bài code:** Làm sạch dữ liệu credit scoring hoặc fraud, baseline logistic.
- **Lab:** Kiểm tra leakage trong đặc trưng.
- **Cổng kiểm tra:** Có baseline và chỉ số đánh giá rõ trước khi thử mô hình mạnh hơn.
- **Không cần học:** AutoML.

### Bước 42: Project 5 (phần 2): Power BI/Excel dashboard
- **Mục tiêu:** Đóng gói project cho người khác đọc
- **Học:** Power BI docs hoặc Tableau Public.
- **Bài tập:** Viết README theo 7 tiêu chuẩn hoàn thành project.
- **Bài code:** XGBoost, SHAP, dashboard Power BI hoặc Excel từ kết quả.
- **Lab:** Thêm mục hạn chế: kết quả không chứng minh điều gì.
- **Cổng kiểm tra:** Project 5 đạt 7 tiêu chuẩn, người khác chạy lại được.
- **Không cần học:** Triển khai production.

### Bước 43: Tuần đệm (làm bù, không học mới)
- **Mục tiêu:** Bù ô còn trống và củng cố chỗ yếu
- **Học:** Xem lại danh sách lỗi đã ghi và chọn 3 chủ đề còn yếu nhất.
- **Bài tập:** Làm lại các bài đã sai hoặc bỏ dở.
- **Bài code:** Dọn code, commit các project đang dở, cập nhật README.
- **Lab:** Chạy lại mọi notebook từ đầu để chắc chắn chạy được.
- **Cổng kiểm tra:** Mọi ô của các tuần trước đã tick, hoặc đã ghi lý do bỏ.
- **Không cần học:** Học nội dung mới.


## Giai đoạn 5: Tài chính và backtest (tuần 44–61)

### Bước 44: Sharpe, Sortino, drawdown
- **Mục tiêu:** Đo hiệu suất như quỹ
- **Học:** Quantitative Trading (Chan): chương đánh giá hiệu suất; Investor.gov.
- **Bài tập:** Tính tay Sharpe, Sortino, max drawdown cho chuỗi 10 ngày.
- **Bài code:** Viết class đánh giá danh mục: nhận chuỗi giá, trả đủ chỉ số.
- **Lab:** Đối chiếu với kết quả của vectorbt.
- **Cổng kiểm tra:** Số của bạn khớp thư viện tới 3 chữ số thập phân.
- **Không cần học:** Omega ratio.

### Bước 45: Kelly, VaR, quản trị vốn
- **Mục tiêu:** Quyết định cỡ lệnh bằng toán
- **Học:** Quantitative Trading (Chan): chương quản trị vốn; Green Book: phần Kelly.
- **Bài tập:** Suy ra Kelly cho cược thắng/thua bằng tay.
- **Bài code:** Mô phỏng Kelly đầy đủ, nửa Kelly, cược cố định; tính VaR lịch sử.
- **Lab:** Backtest VaR 95% và đếm số lần vi phạm.
- **Cổng kiểm tra:** Giải thích vì sao Kelly đầy đủ rủi ro cao trong thực tế.
- **Không cần học:** Expected Shortfall nâng cao.

### Bước 46: Danh mục: Markowitz, CAPM, CVXPY
- **Mục tiêu:** Tối ưu danh mục có ràng buộc thực tế
- **Học:** CVXPY: ví dụ portfolio optimization; Bodie–Kane–Marcus, Investments: chương Markowitz và CAPM.
- **Bài tập:** Suy ra danh mục phương sai tối thiểu bằng Lagrange.
- **Bài code:** CVXPY: tối ưu Markowitz VN30, tỷ trọng tối đa 20%, dùng Ledoit-Wolf.
- **Lab:** Vẽ biên hiệu quả.
- **Cổng kiểm tra:** So danh mục tối ưu với chia đều 1/N ngoài mẫu và giải thích.
- **Không cần học:** Black-Litterman.

### Bước 47: Tài chính nền: lãi suất, trái phiếu, báo cáo tài chính
- **Mục tiêu:** Hiểu ngôn ngữ thị trường trước khi mô hình hóa
- **Học:** Khan Academy: Finance and capital markets (mục lãi suất, trái phiếu, cổ phiếu); Investor.gov: cách đọc báo cáo tài chính (bảng cân đối, kết quả kinh doanh, lưu chuyển tiền tệ).
- **Bài tập:** Tính tay giá trị hiện tại và lợi suất đáo hạn của trái phiếu 3 năm; đọc báo cáo tài chính một công ty VN30 và tính ROE, P/E.
- **Bài code:** Viết hàm tính PV, YTM và vẽ quan hệ giá trái phiếu với lãi suất.
- **Lab:** Tự tính ROE và P/E của một mã từ số liệu trong báo cáo, không dùng web tính sẵn.
- **Cổng kiểm tra:** Giải thích vì sao lãi suất tăng thì giá trái phiếu giảm, kèm số liệu.
- **Không cần học:** Phái sinh lãi suất, kế toán nâng cao.

### Bước 48: Mô hình nhân tố: CAPM và Fama-French
- **Mục tiêu:** Biết lợi suất cổ phiếu được giải thích bằng những nhân tố nào
- **Học:** Bodie–Kane–Marcus, Investments: chương mô hình đa nhân tố; Kenneth French Data Library: mô tả các nhân tố thị trường, quy mô, giá trị.
- **Bài tập:** Ước lượng beta bằng tay (cov/var) cho 3 cổ phiếu so với chỉ số.
- **Bài code:** Hồi quy lợi suất 10 mã VN30 theo thị trường, rồi thêm một nhân tố tự dựng (động lượng 12 tháng); so R-squared.
- **Lab:** Phân biệt alpha và beta trong kết quả hồi quy.
- **Cổng kiểm tra:** Giải thích alpha và beta của một mã bằng lời và nói alpha có ý nghĩa thống kê hay không.
- **Không cần học:** APT chi tiết, mô hình 5 nhân tố.

### Bước 49: Kinh tế lượng tài chính: hồi quy giả, sai số chuẩn HAC
- **Mục tiêu:** Tránh kết luận sai khi hồi quy dữ liệu giá
- **Học:** Ruppert, Statistics and Data Analysis for Financial Engineering: chương hồi quy và chuỗi thời gian; tài liệu statsmodels: sai số chuẩn HAC (Newey-West).
- **Bài tập:** Giải thích bằng lời vì sao hồi quy hai chuỗi giá (không dừng) có thể cho R-squared cao mà vô nghĩa.
- **Bài code:** Mô phỏng 2 bước ngẫu nhiên độc lập, hồi quy chúng, đếm tỷ lệ p<0.05; so sai số chuẩn thường với HAC trên hồi quy lợi suất BTC–ETH.
- **Lab:** Lặp lại thí nghiệm trên lợi suất thay vì giá.
- **Cổng kiểm tra:** Chứng minh bằng mô phỏng rằng hồi quy giá với giá cho kết quả có ý nghĩa giả, và nêu cách tránh.
- **Không cần học:** Hồi quy panel, GMM.

### Bước 50: Stochastic calculus nhập môn: Brownian motion, Itô
- **Mục tiêu:** Hiểu nguồn gốc của Black-Scholes, không học thuộc công thức
- **Học:** Hull, Options, Futures and Other Derivatives: chương quá trình Wiener và bổ đề Itô; Shreve, Stochastic Calculus for Finance II: chương 3 và phần đầu chương 4 (đọc trực giác, bỏ chứng minh).
- **Bài tập:** Tính tay E[W_t], Var[W_t]; dùng bổ đề Itô để ra phương trình của ln S khi giá theo GBM.
- **Bài code:** Mô phỏng 1.000 đường Brownian motion và GBM bằng NumPy; kiểm tra giá cuối kỳ có phân phối log-chuẩn.
- **Lab:** So kỳ vọng và phương sai mô phỏng với công thức lý thuyết.
- **Cổng kiểm tra:** Giải thích bằng lời vì sao ln S có độ trôi μ - σ²/2 chứ không phải μ.
- **Không cần học:** Chứng minh chặt chẽ, đổi độ đo, Girsanov.

### Bước 51: Quyền chọn 1: Black-Scholes
- **Mục tiêu:** Định giá quyền chọn cơ bản
- **Học:** Hull: chương Black-Scholes-Merton; Green Book: phần option.
- **Bài tập:** Tính tay giá call bằng cây nhị phân 2 bước.
- **Bài code:** Cài Black-Scholes bằng Python, so với cây nhị phân.
- **Lab:** Vẽ giá option theo giá cơ sở.
- **Cổng kiểm tra:** Tính được giá option bằng tay hoặc Excel.
- **Không cần học:** Stochastic calculus sâu.

### Bước 52: Quyền chọn 2: Greeks, put-call parity
- **Mục tiêu:** Hiểu độ nhạy của option
- **Học:** Hull: chương Greeks; Green Book: put-call parity.
- **Bài tập:** Tính tay Delta, Gamma của call; kiểm chứng put-call parity.
- **Bài code:** Tính Greeks bằng Python và mô phỏng delta hedging.
- **Lab:** Đo sai số hedge khi đổi tần suất hedge.
- **Cổng kiểm tra:** Giải thích Delta, Gamma, Vega bằng lời.
- **Không cần học:** Exotic options.

### Bước 53: Tự viết backtest bằng pandas
- **Mục tiêu:** Hiểu bản chất trước khi dùng thư viện
- **Học:** vectorbt và backtesting.py: chỉ đọc quickstart.
- **Bài tập:** Viết logic tín hiệu và vào lệnh trên giấy.
- **Bài code:** Tự viết backtest cắt chéo MA bằng pandas, chia in-sample và out-of-sample.
- **Lab:** Đối chiếu kết quả với backtesting.py.
- **Cổng kiểm tra:** Giải thích vì sao tín hiệu phải shift 1 kỳ.
- **Không cần học:** Event-driven phức tạp.

### Bước 54: Bẫy dữ liệu backtest: survivorship, giá điều chỉnh
- **Mục tiêu:** Tránh các lỗi dữ liệu làm backtest đẹp giả
- **Học:** Tài liệu nhà cung cấp dữ liệu về giá điều chỉnh (chia tách, cổ tức); Chan: phần survivorship bias.
- **Bài tập:** Liệt kê 5 cách dữ liệu làm backtest đẹp giả: coin đã chết, cổ phiếu hủy niêm yết, dùng danh sách VN30 hiện tại cho quá khứ, giá chưa điều chỉnh, dữ liệu bị sửa về sau.
- **Bài code:** Backtest cùng chiến lược với giá điều chỉnh và chưa điều chỉnh; với danh sách mã hiện tại và danh sách mã theo từng thời điểm.
- **Lab:** Đo chênh lệch kết quả, ghi vào README của Project 4.
- **Cổng kiểm tra:** Chỉ ra bẫy nào ảnh hưởng nhất đến dữ liệu của bạn và cách giảm.
- **Không cần học:** Dữ liệu point-in-time trả phí.

### Bước 55: Chi phí, slippage, thị trường VN, phái sinh crypto
- **Mục tiêu:** Để backtest gần với thực tế
- **Học:** HOSE (hsx.vn): quy định giao dịch hiện hành; tài liệu sàn về funding rate và thanh lý.
- **Bài tập:** Liệt kê quy tắc thị trường VN cần đưa vào backtest. Lưu ý: cá nhân thường không bán khống được cổ phiếu VN (kiểm tra quy định hiện hành), nên chiến lược long-short chủ yếu thử trên crypto.
- **Bài code:** Thêm phí, slippage, lô chẵn 100 cổ phiếu, biên độ giá vào backtest.
- **Lab:** Đo lợi nhuận còn lại sau chi phí.
- **Cổng kiểm tra:** Kiểm tra quy định hiện hành trước khi backtest VN30.
- **Không cần học:** Phái sinh VN.

### Bước 56: Pairs trading, cointegration
- **Mục tiêu:** Giao dịch cặp tài sản
- **Học:** Algorithmic Trading (Chan, 2013): chương mean reversion, cointegration.
- **Bài tập:** Phân biệt tương quan và đồng liên kết bằng ví dụ. Ưu tiên thử trên crypto; với cổ phiếu VN xem lưu ý về bán khống ở tuần chi phí.
- **Bài code:** Tìm cặp cointegrated, vẽ spread, kiểm tra bằng ADF.
- **Lab:** Backtest pairs có chi phí.
- **Cổng kiểm tra:** Giải thích vì sao tương quan cao chưa chắc đồng liên kết.
- **Không cần học:** Kalman filter cho hedge ratio.

### Bước 57: Nghiên cứu alpha: rank, neutralization
- **Mục tiêu:** Xây tín hiệu theo cách các quỹ làm
- **Học:** WorldQuant Learn2Quant; nền tảng BRAIN.
- **Bài tập:** Làm bài về rank và chuẩn hóa tín hiệu.
- **Bài code:** Xây tín hiệu alpha, rank cắt ngang mã, neutralize theo thị trường.
- **Lab:** Tính IC của tín hiệu.
- **Cổng kiểm tra:** Giải thích rank và neutralization giải quyết vấn đề gì.
- **Không cần học:** Alpha phức tạp.

### Bước 58: Project 4 (phần 1): chiến lược và tín hiệu
- **Mục tiêu:** Bắt đầu dự án quan trọng nhất
- **Học:** Quantitative Trading (Chan); vectorbt docs.
- **Bài tập:** Viết giả thuyết chiến lược và tiêu chí đánh giá trước khi chạy.
- **Bài code:** Dựng pipeline dữ liệu và tín hiệu cho BTC hoặc VN30.
- **Lab:** Chốt baseline buy-and-hold.
- **Cổng kiểm tra:** Giả thuyết và tiêu chí được ghi trước khi nhìn kết quả.
- **Không cần học:** Chiến lược mới.

### Bước 59: Project 4 (phần 2): overfitting, Deflated Sharpe
- **Mục tiêu:** Đánh giá trung thực
- **Học:** López de Prado: chương thống kê backtest (Deflated Sharpe).
- **Bài tập:** Đếm và ghi số biến thể đã thử.
- **Bài code:** Chạy backtest có phí, tính Deflated Sharpe.
- **Lab:** Đánh giá out-of-sample bằng walk-forward.
- **Cổng kiểm tra:** Ghi đủ số biến thể đã thử và kết quả trừ phí.
- **Không cần học:** Tối ưu tham số thêm.

### Bước 60: Project 4 hoàn thiện: README “Vì sao kết quả có thể là ảo”
- **Mục tiêu:** Hoàn thiện dự án quan trọng nhất
- **Học:** Cách viết README project (7 tiêu chuẩn).
- **Bài tập:** Viết mục “Vì sao kết quả này có thể là ảo”.
- **Bài code:** Hoàn thiện biểu đồ, README tiếng Anh, test.
- **Lab:** Nhờ AI đóng vai người phỏng vấn vặn về project.
- **Cổng kiểm tra:** Project 4 đạt 7 tiêu chuẩn và so với buy-and-hold.
- **Không cần học:** Tính năng mới.

### Bước 61: Tuần đệm (làm bù, không học mới)
- **Mục tiêu:** Bù ô còn trống và củng cố chỗ yếu
- **Học:** Xem lại danh sách lỗi đã ghi và chọn 3 chủ đề còn yếu nhất.
- **Bài tập:** Làm lại các bài đã sai hoặc bỏ dở.
- **Bài code:** Dọn code, commit các project đang dở, cập nhật README.
- **Lab:** Chạy lại mọi notebook từ đầu để chắc chắn chạy được.
- **Cổng kiểm tra:** Mọi ô của các tuần trước đã tick, hoặc đã ghi lý do bỏ.
- **Không cần học:** Học nội dung mới.


## Giai đoạn 6: Phỏng vấn và nộp đơn (tuần 62–69)

### Bước 62: Giải thuật 1: Big-O, mảng, hash map
- **Mục tiêu:** Rèn tư duy cho vòng code
- **Học:** NeetCode Roadmap: Arrays & Hashing, Two Pointers, Sliding Window; VisuAlgo.
- **Bài tập:** Giải 15 bài LeetCode Easy về mảng và hash map.
- **Bài code:** Cài Two Pointers và Sliding Window bằng Python.
- **Lab:** Ghi Big-O mỗi bài.
- **Cổng kiểm tra:** Giải bài Easy trong 15–20 phút và giải thích Big-O.
- **Không cần học:** Đồ thị, DP.

### Bước 63: Giải thuật 2: stack, heap, binary search, đệ quy
- **Mục tiêu:** Cấu trúc dữ liệu còn lại
- **Học:** NeetCode: Stack, Binary Search, Heap, đệ quy, Trees, Graphs (BFS/DFS bản cơ bản).
- **Bài tập:** Giải 15 bài Medium.
- **Bài code:** Cài binary search và heap bằng Python.
- **Lab:** Giải lại bài đã sai.
- **Cổng kiểm tra:** Giải 1 bài Medium trong 30 phút.
- **Không cần học:** Đồ thị nâng cao.

### Bước 64: Brain Teasers xác suất 1
- **Mục tiêu:** Luyện đề phỏng vấn quant
- **Học:** Green Book: các chương xác suất và brain teasers.
- **Bài tập:** Tự giải 20 bài trước khi xem lời giải.
- **Bài code:** Kiểm chứng 5 bài bằng mô phỏng Python.
- **Lab:** Ghi lại các dạng bài hay sai.
- **Cổng kiểm tra:** Giải 70% bài tự lực.
- **Không cần học:** Sách khác.

### Bước 65: Brain Teasers 2 và câu hỏi thống kê
- **Mục tiêu:** Nói to cách tư duy
- **Học:** Green Book: phần thống kê và option; Heard on the Street.
- **Bài tập:** Tự giải 20 bài.
- **Bài code:** Mô phỏng các bài khó.
- **Lab:** Tập nói to cách giải trong 3 phút.
- **Cổng kiểm tra:** Nói to cách giải một bài chưa thấy, có bấm giờ.
- **Không cần học:** Bài quá khó.

### Bước 66: Tiếng Anh kỹ thuật: README, CV
- **Mục tiêu:** Trình bày project bằng tiếng Anh
- **Học:** Đọc 3 README project nổi tiếng trên GitHub.
- **Bài tập:** Viết lại README Project 4 bằng tiếng Anh.
- **Bài code:** Thu video 5 phút giải thích project bằng tiếng Anh.
- **Lab:** Dịch 10 thuật ngữ: p-value, bias-variance, drawdown.
- **Cổng kiểm tra:** Giải thích một project 5 phút bằng tiếng Anh, không đọc script.
- **Không cần học:** Luyện thi chứng chỉ.

### Bước 67: Project tổng hợp: SQL, Python, kiểm tra dữ liệu, báo cáo
- **Mục tiêu:** Gom mọi công cụ vào một dự án
- **Học:** Xem lại 7 tiêu chuẩn hoàn thành project.
- **Bài tập:** Lập kế hoạch: SQL, Python, kiểm tra dữ liệu, thống kê, báo cáo.
- **Bài code:** Dựng project cuối gom công cụ đã học.
- **Lab:** Viết giải thích từng quyết định thiết kế.
- **Cổng kiểm tra:** Giải thích được mọi quyết định trong project.
- **Không cần học:** Công nghệ mới.

### Bước 68: CV, GitHub, phỏng vấn thử với AI
- **Mục tiêu:** Sẵn sàng để nộp
- **Học:** Mẫu CV kỹ thuật một trang; GitHub profile README.
- **Bài tập:** Viết CV tiếng Anh với 4–5 project.
- **Bài code:** Dọn repo: README, cấu trúc, test.
- **Lab:** Phỏng vấn thử với AI đóng vai người hỏi khó.
- **Cổng kiểm tra:** CV một trang và 4 repo chạy lại được.
- **Không cần học:** Thiết kế CV cầu kỳ.

### Bước 69: Nộp đơn, phỏng vấn thật, vá lỗ hổng
- **Mục tiêu:** Thực chiến và học từ thất bại
- **Học:** DataLemur, StrataScratch: luyện câu hỏi SQL và phân tích thật.
- **Bài tập:** Làm 20 câu SQL và thống kê của công ty thật.
- **Bài code:** Nộp ít nhất 5 vị trí thực tập, ghi lại mọi câu hỏi.
- **Lab:** Vá lỗ hổng từ câu hỏi đã gặp.
- **Cổng kiểm tra:** Hoàn thành ít nhất 3 buổi phỏng vấn thật hoặc thử.
- **Không cần học:** Chờ hoàn hảo mới nộp.
