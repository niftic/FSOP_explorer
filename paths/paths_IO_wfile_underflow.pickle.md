# _IO_wfile_underflow.pickle
2 states with [10, 11] frames
## State 0 with ending 0x86e12
### Frame 0: `_IO_wfile_underflow`
~~~asm
       _IO_wfile_underflow:
85050  endbr64 
85054  push    r15
85056  push    r14
85058  push    r13
8505a  push    r12
8505c  push    rbp
8505d  push    rbx
8505e  sub     rsp, 0x68
85062  mov     rax, qword ptr  fs:[0x28]
8506b  mov     qword ptr [rsp+0x58], rax
85070  mov     eax, dword ptr [rdi]
85072  test    al, errno
85074  jne     0x85209
~~~
### Frame 1: `_IO_wfile_underflow+42`
~~~asm
8507a  mov     rbx, rdi
8507d  test    al, 0x4
8507f  jne     0x85658
~~~
### Frame 2: `_IO_wfile_underflow+53`
~~~asm
85085  mov     rax, qword ptr [rdi+0xa0]
8508c  mov     rdx, qword ptr [rax]
8508f  cmp     rdx, qword ptr [rax+__resp]
85093  jb      0x851c8
~~~
### Frame 3: `_IO_wfile_underflow+73`
~~~asm
85099  mov     rdx, qword ptr [rdi+__resp]
8509d  mov     rcx, qword ptr [rdi+errno]
850a1  mov     r14, qword ptr [rdi+0x98]
850a8  cmp     rdx, rcx
850ab  jb      0x85500
~~~
### Frame 4: `_IO_wfile_underflow+1200`
~~~asm
85500  mov     r9, qword ptr [rax+0x30]
85504  mov     rsi, qword ptr [rax+0x58]
85508  lea     rdi, [rax+__resp]
8550c  mov     qword ptr [rsp+0x38], rdx
85511  mov     qword ptr [rax+0x60], rsi
85515  lea     rsi, [rax+0x58]
85519  mov     qword ptr [rax], r9
8551c  mov     qword ptr [rax+errno], r9
85520  push    rdi
85521  mov     rdi, r14
85524  push    qword ptr [rax+0x38]
85527  lea     r8, [rsp+0x48]
8552c  call    0x86d80
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
- `_IO_wfile_underflow`
  - `__libio_codecvt_in`
    - `[_codecvt->__cd_in[63:0] + 0x28]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 16) == 0
(_flags[7:0] & 4) == 0
_wide_data->_IO_read_ptr >= _wide_data->_IO_read_end
_IO_read_ptr < _IO_read_end
[_codecvt->__cd_in[63:0]] == 0x0
~~~
--------------------
Register values at the call:
- `rax`: 0x33a040
- `rcx`: _IO_read_end
- `rdx`: 0x7fffffffffeff00
- `rbx`: _codecvt
- `rsp`: 0x7fffffffffefec8
- `rbp`: [_codecvt->__cd_in[63:0] + 0x28]
- `rsi`: 0x8 + _codecvt
- `rdi`: _codecvt->__cd_in[63:0]
- `r8`: 0x0
- `r9`: 0x7fffffffffefef8
- `r10`: 0x58 + _wide_data
- `r11`: orig_r11
- `r12`: 0x7fffffffffeff98
- `r13`: _codecvt->__cd_in[63:0]
- `r14`: 0x8 + _wide_data
- `r15`: _IO_read_end
- `rip`: [_codecvt->__cd_in[63:0] + 0x28]
------------------------------
## State 1 with ending 0x83c1b
### Frame 0: `_IO_wfile_underflow`
~~~asm
       _IO_wfile_underflow:
85050  endbr64 
85054  push    r15
85056  push    r14
85058  push    r13
8505a  push    r12
8505c  push    rbp
8505d  push    rbx
8505e  sub     rsp, 0x68
85062  mov     rax, qword ptr  fs:[0x28]
8506b  mov     qword ptr [rsp+0x58], rax
85070  mov     eax, dword ptr [rdi]
85072  test    al, errno
85074  jne     0x85209
~~~
### Frame 1: `_IO_wfile_underflow+42`
~~~asm
8507a  mov     rbx, rdi
8507d  test    al, 0x4
8507f  jne     0x85658
~~~
### Frame 2: `_IO_wfile_underflow+53`
~~~asm
85085  mov     rax, qword ptr [rdi+0xa0]
8508c  mov     rdx, qword ptr [rax]
8508f  cmp     rdx, qword ptr [rax+__resp]
85093  jb      0x851c8
~~~
### Frame 3: `_IO_wfile_underflow+73`
~~~asm
85099  mov     rdx, qword ptr [rdi+__resp]
8509d  mov     rcx, qword ptr [rdi+errno]
850a1  mov     r14, qword ptr [rdi+0x98]
850a8  cmp     rdx, rcx
850ab  jb      0x85500
~~~
### Frame 4: `_IO_wfile_underflow+97`
~~~asm
850b1  mov     rax, qword ptr [rdi+0x38]
850b5  movq    xmm0, rax
850ba  mov     qword ptr [rdi+0x18], rax
850be  punpcklqdq xmm0, xmm0
850c2  movups  xmmword ptr [rdi+__resp], xmm0
850c6  movq    xmm0, rax
850cb  punpcklqdq xmm0, xmm0
850cf  test    rax, rax
850d2  je      0x855c8
~~~
### Frame 5: `_IO_wfile_underflow+136`
~~~asm
850d8  mov     qword ptr [rbx+0x30], rax
850dc  mov     rax, qword ptr [rbx+0xa0]
850e3  movups  xmmword ptr [rbx+0x20], xmm0
850e7  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
850ec  je      0x855a0
~~~
### Frame 6: `_IO_wfile_underflow+1360`
~~~asm
855a0  mov     rdi, qword ptr [rax+__libc_dlerror_result]
855a4  test    rdi, rdi
855a7  je      0x855b4
~~~
### Frame 7: `_IO_wfile_underflow+1380`
~~~asm
855b4  mov     rdi, rbx
855b7  call    _IO_wdoallocbuf
~~~
### Frame 8: `_IO_wdoallocbuf`
~~~asm
       _IO_wdoallocbuf:
83bf0  endbr64 
83bf4  mov     rax, qword ptr [rdi+0xa0]
83bfb  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
83c00  je      0x83c08
~~~
### Frame 9: `_IO_wdoallocbuf+24`
~~~asm
83c08  push    r12
83c0a  push    rbp
83c0b  push    rbx
83c0c  mov     rbx, rdi
83c0f  test    byte ptr [rdi], 0x2
83c12  jne     0x83c88
~~~
### Frame 10: `_IO_wdoallocbuf+36`
~~~asm
83c14  mov     rax, qword ptr [rax+0xe0]
83c1b  call    qword ptr [rax+0x68]
~~~
--------------------
Call stack:
- `_IO_wfile_underflow`
  - `_IO_wdoallocbuf`
    - `[_wide_data->_wide_vtable + 0x68]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 16) == 0
(_flags[7:0] & 4) == 0
_wide_data->_IO_read_ptr >= _wide_data->_IO_read_end
_IO_read_ptr >= _IO_read_end
_IO_buf_base != 0x0
_wide_data->_IO_buf_base == 0x0
_wide_data->_IO_save_base == 0x0
_wide_data->_IO_buf_base == 0x0
(_flags[7:0] & 2) == 0
~~~
--------------------
Register values at the call:
- `rax`: _wide_data->_wide_vtable
- `rcx`: _IO_read_end
- `rdx`: _IO_read_ptr
- `rbx`: fp
- `rsp`: 0x7fffffffffeff38
- `rbp`: orig_rbp
- `rsi`: orig_rsi
- `rdi`: fp
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: orig_r12
- `r13`: orig_r13
- `r14`: _codecvt
- `r15`: orig_r15
- `rip`: [_wide_data->_wide_vtable + 0x68]
------------------------------
