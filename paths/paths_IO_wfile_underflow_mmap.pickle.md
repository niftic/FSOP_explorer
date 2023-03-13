# _IO_wfile_underflow_mmap.pickle
3 states with [9, 10, 17] frames
## State 0 with ending 0x83c1b
### Frame 0: `_IO_wfile_underflow_mmap`
~~~asm
860b0  endbr64 
860b4  push    rbp
860b5  push    rbx
860b6  mov     rbx, rdi
860b9  sub     rsp, 0x18
860bd  mov     rax, qword ptr  fs:[0x28]
860c6  mov     qword ptr [rsp+__resp], rax
860cb  mov     eax, dword ptr [rdi]
860cd  test    al, 0x4
860cf  jne     0x861f0
~~~
### Frame 1: `_IO_wfile_underflow_mmap+37`
~~~asm
860d5  mov     rax, qword ptr [rdi+0xa0]
860dc  mov     rdx, qword ptr [rax]
860df  cmp     rdx, qword ptr [rax+__resp]
860e3  jb      0x86170
~~~
### Frame 2: `_IO_wfile_underflow_mmap+57`
~~~asm
860e9  mov     rbp, qword ptr [rdi+0x98]
860f0  mov     rdx, qword ptr [rdi+__resp]
860f4  cmp     rdx, qword ptr [rdi+errno]
860f8  jae     0x86190
~~~
### Frame 3: `_IO_wfile_underflow_mmap+78`
~~~asm
860fe  mov     r9, qword ptr [rax+0x30]
86102  mov     qword ptr [rsp], rdx
86106  test    r9, r9
86109  je      0x861b6
~~~
### Frame 4: `_IO_wfile_underflow_mmap+262`
~~~asm
861b6  mov     rdi, qword ptr [rax+__libc_dlerror_result]
861ba  test    rdi, rdi
861bd  je      0x861ca
~~~
### Frame 5: `_IO_wfile_underflow_mmap+282`
~~~asm
861ca  mov     rdi, rbx
861cd  call    _IO_wdoallocbuf
~~~
### Frame 6: `_IO_wdoallocbuf`
~~~asm
       _IO_wdoallocbuf:
83bf0  endbr64 
83bf4  mov     rax, qword ptr [rdi+0xa0]
83bfb  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
83c00  je      0x83c08
~~~
### Frame 7: `_IO_wdoallocbuf+24`
~~~asm
83c08  push    r12
83c0a  push    rbp
83c0b  push    rbx
83c0c  mov     rbx, rdi
83c0f  test    byte ptr [rdi], 0x2
83c12  jne     0x83c88
~~~
### Frame 8: `_IO_wdoallocbuf+36`
~~~asm
83c14  mov     rax, qword ptr [rax+0xe0]
83c1b  call    qword ptr [rax+0x68]
~~~
--------------------
Call stack:
- `_IO_wfile_underflow_mmap`
  - `_IO_wdoallocbuf`
    - `[_wide_data->_wide_vtable + 0x68]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 4) == 0
_wide_data->_IO_read_ptr >= _wide_data->_IO_read_end
_IO_read_ptr < _IO_read_end
_wide_data->_IO_buf_base == 0x0
_wide_data->_IO_save_base == 0x0
_wide_data->_IO_buf_base == 0x0
(_flags[7:0] & 2) == 0
~~~
--------------------
Register values at the call:
- `rax`: _wide_data->_wide_vtable
- `rcx`: orig_rcx
- `rdx`: _IO_read_ptr
- `rbx`: fp
- `rsp`: 0x7fffffffffeffa8
- `rbp`: _codecvt
- `rsi`: orig_rsi
- `rdi`: fp
- `r8`: orig_r8
- `r9`: _wide_data->_IO_buf_base
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: orig_r12
- `r13`: orig_r13
- `r14`: orig_r14
- `r15`: orig_r15
- `rip`: [_wide_data->_wide_vtable + 0x68]
------------------------------
## State 1 with ending 0x86e12
### Frame 0: `_IO_wfile_underflow_mmap`
~~~asm
860b0  endbr64 
860b4  push    rbp
860b5  push    rbx
860b6  mov     rbx, rdi
860b9  sub     rsp, 0x18
860bd  mov     rax, qword ptr  fs:[0x28]
860c6  mov     qword ptr [rsp+__resp], rax
860cb  mov     eax, dword ptr [rdi]
860cd  test    al, 0x4
860cf  jne     0x861f0
~~~
### Frame 1: `_IO_wfile_underflow_mmap+37`
~~~asm
860d5  mov     rax, qword ptr [rdi+0xa0]
860dc  mov     rdx, qword ptr [rax]
860df  cmp     rdx, qword ptr [rax+__resp]
860e3  jb      0x86170
~~~
### Frame 2: `_IO_wfile_underflow_mmap+57`
~~~asm
860e9  mov     rbp, qword ptr [rdi+0x98]
860f0  mov     rdx, qword ptr [rdi+__resp]
860f4  cmp     rdx, qword ptr [rdi+errno]
860f8  jae     0x86190
~~~
### Frame 3: `_IO_wfile_underflow_mmap+78`
~~~asm
860fe  mov     r9, qword ptr [rax+0x30]
86102  mov     qword ptr [rsp], rdx
86106  test    r9, r9
86109  je      0x861b6
~~~
### Frame 4: `_IO_wfile_underflow_mmap+95`
~~~asm
8610f  mov     rcx, qword ptr [rax+0x58]
86113  lea     rdi, [rax+__resp]
86117  mov     qword ptr [rax], r9
8611a  lea     rsi, [rax+0x58]
8611e  mov     qword ptr [rax+errno], r9
86122  mov     qword ptr [rax+0x60], rcx
86126  mov     rcx, qword ptr [rbx+errno]
8612a  push    rdi
8612b  mov     rdi, rbp
8612e  push    qword ptr [rax+0x38]
86131  lea     r8, [rsp+errno]
86136  call    0x86d80
~~~
### Frame 5: `__libio_codecvt_in`
~~~asm
86d80  endbr64 
86d84  push    r15
86d86  movq    xmm0, r9
86d8b  mov     r10, rsi
86d8e  mov     r15, rcx
86d91  push    r14
86d93  lea     rsi, [rdi+__resp]
86d97  push    r13
86d99  push    r12
86d9b  mov     r12, r8
86d9e  push    rbp
86d9f  push    rbx
86da0  mov     rbx, rdi
86da3  sub     rsp, 0x38
86da7  mov     r13, qword ptr [rdi]
86daa  mov     rax, qword ptr  fs:[0x28]
86db3  mov     qword ptr [rsp+0x28], rax
86db8  xor     eax, eax
86dba  movhps  xmm0, qword ptr [rsp+0x70]
86dbf  mov     qword ptr [rdi+0x28], r10
86dc3  mov     r14, qword ptr [rsp+0x78]
86dc8  cmp     qword ptr [r13], GLIBC_PRIVATE
86dcd  mov     rbp, qword ptr [r13+0x28]
86dd1  mov     qword ptr [rsp+0x20], rdx
86dd6  movups  xmmword ptr [rdi+__resp], xmm0
86dda  je      0x86de9
~~~
### Frame 6: `__libio_codecvt_in+105`
~~~asm
86de9  mov     rdi, rbp
86dec  mov     qword ptr [rsp+__resp], rsi
86df1  call    _dl_mcount_wrapper_check
~~~
### Frame 7: `_dl_mcount_wrapper_check`
~~~asm
        _dl_mcount_wrapper_check:
1754d0  endbr64 
1754d4  mov     rax, qword ptr [0x218fa0]
1754db  mov     rsi, rdi
1754de  cmp     qword ptr [rax+0xa90], GLIBC_PRIVATE
1754e6  je      0x175500
~~~
### Frame 8: `_dl_mcount_wrapper_check+48`
~~~asm
175500  ret     
~~~
### Frame 9: `__libio_codecvt_in+118`
~~~asm
86df6  lea     rdx, [rsp+0x20]
86dfb  push    GLIBC_PRIVATE
86dfd  mov     rcx, r15
86e00  push    GLIBC_PRIVATE
86e02  xor     r8d, r8d
86e05  mov     rsi, qword ptr [rsp+0x18]
86e0a  mov     rdi, r13
86e0d  lea     r9, [rsp+0x28]
86e12  call    rbp
~~~
--------------------
Call stack:
- `_IO_wfile_underflow_mmap`
  - `__libio_codecvt_in`
    - `[_codecvt->__cd_in[63:0] + 0x28]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 4) == 0
_wide_data->_IO_read_ptr >= _wide_data->_IO_read_end
_IO_read_ptr < _IO_read_end
_wide_data->_IO_buf_base != 0x0
[_codecvt->__cd_in[63:0]] == 0x0
~~~
--------------------
Register values at the call:
- `rax`: 0x33a040
- `rcx`: _IO_read_end
- `rdx`: 0x7fffffffffeff70
- `rbx`: _codecvt
- `rsp`: 0x7fffffffffeff38
- `rbp`: [_codecvt->__cd_in[63:0] + 0x28]
- `rsi`: 0x8 + _codecvt
- `rdi`: _codecvt->__cd_in[63:0]
- `r8`: 0x0
- `r9`: 0x7fffffffffeff68
- `r10`: 0x58 + _wide_data
- `r11`: orig_r11
- `r12`: 0x7fffffffffeffd0
- `r13`: _codecvt->__cd_in[63:0]
- `r14`: 0x8 + _wide_data
- `r15`: _IO_read_end
- `rip`: [_codecvt->__cd_in[63:0] + 0x28]
------------------------------
