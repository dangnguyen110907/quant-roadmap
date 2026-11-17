# SỔ TAY GHI LỖI (LOI.MD)

Nơi ghi lại các lỗi đã gặp, nguyên nhân gốc rễ và bài học rút ra để không lặp lại.

---

## MẪU GHI LỖI (TEMPLATE)
```markdown
### [Ngày] - [Module / Bài tập] - [Tên lỗi]
- **Hiện tượng:** Lỗi hiển thị gì / Test fail chỗ nào?
- **Nguyên nhân gốc rễ:** Do hiểu sai khái niệm gì?
- **Cách khắc phục:** Sửa lại như thế nào?
```

---

## DANH SÁCH LỖI ĐÃ TỔNG HỢP

### 2026-11-14 - Module 1: Git - Lỗi không tìm thấy nhánh khi merge
- **Hiện tượng:** Gõ `git merge feature-notes` báo lỗi `merge: feature-notes - not something we can merge`.
- **Nguyên nhân gốc rễ:** Lúc tạo nhánh đặt tên dùng dấu gạch dưới `feature_notes`, nhưng lúc merge lại gõ dấu gạch ngang `feature-notes`.
- **Cách khắc phục:** Gõ đúng tên `git merge feature_notes`. Dùng phím `Tab` để autocomplete tên nhánh, tránh gõ tay.

### 2026-11-14 - Module 2: Python - Chuỗi (String) là bất biến (Immutable)
- **Hiện tượng:** Chạy `d.replace("$", "")` nhưng biến `d` vẫn giữ nguyên dấu `$`, dẫn đến `ValueError: could not convert string to float`.
- **Nguyên nhân gốc rễ:** Chuỗi trong Python không thể bị thay đổi tại chỗ (immutable). Phương thức `.replace()` trả về chuỗi mới chứ không sửa biến cũ.
- **Cách khắc phục:** Phải gán lại: `d = d.replace("$", "")`.

### 2026-11-14 - Module 2: Python - So sánh chuỗi chính xác vs Tiền tố
- **Hiện tượng:** `test_bank.py` fail khi kiểm tra `"Hello, Newman"`.
- **Nguyên nhân gốc rễ:** Dùng `greeting == "hello"` thay vì kiểm tra tiền tố bắt đầu bằng `"hello"`.
- **Cách khắc phục:** Dùng phương thức `greeting.startswith("hello")`.

### 2026-11-14 - Module 2: Python - Nhầm lẫn toán tử biên (Fuel Gauge)
- **Hiện tượng:** 1% bị hiển thị thành số thay vì chữ `E`.
- **Nguyên nhân gốc rễ:** Viết điều kiện `< 1` thay vì `<= 1`.
- **Cách khắc phục:** Đổi thành `if percent <= 1: return "E"`.
