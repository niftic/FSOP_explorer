# _IO_file_setbuf_mmap.pickle
2 states with [17, 18] frames
## State 0 with ending 0x86d13
### Frame 0: `_IO_file_setbuf_mmap`
~~~asm
8a650  endbr64 
8a654  lea     rax, [_IO_file_jumps]
8a65b  lea     rcx, [_IO_wfile_jumps]
8a662  push    rbx
8a663  mov     rbx, rdi
8a666  mov     qword ptr [rdi+0xd8], rax
8a66d  mov     rax, qword ptr [rdi+0xa0]
8a674  mov     qword ptr [rax+0xe0], rcx
8a67b  call    _IO_file_setbuf
~~~
### Frame 1: `_IO_file_setbuf`
~~~asm
       _IO_file_setbuf:
8a620  endbr64 
8a624  push    rbx
8a625  mov     rbx, rdi
8a628  call    0x8e430
~~~
### Frame 2: `_IO_default_setbuf`
~~~asm
8e430  endbr64 
8e434  push    r13
8e436  lea     rax, [0x216768]
8e43d  push    r12
8e43f  mov     r12, rdx
8e442  lea     rdx, [0x215a00]
8e449  push    rbp
8e44a  sub     rax, rdx
8e44d  mov     rbp, rsi
8e450  push    rbx
8e451  mov     rbx, rdi
8e454  sub     rsp, __resp
8e458  mov     r13, qword ptr [rdi+0xd8]
8e45f  mov     rcx, r13
8e462  sub     rcx, rdx
8e465  cmp     rax, rcx
8e468  jbe     0x8e510
~~~
### Frame 3: `_IO_default_setbuf+62`
~~~asm
8e46e  mov     rdi, rbx
8e471  call    qword ptr [r13+0x60]
~~~
### Frame 4: `_IO_file_sync`
~~~asm
       _IO_file_sync:
8a4b0  endbr64 
8a4b4  push    rbp
8a4b5  push    rbx
8a4b6  mov     rbx, rdi
8a4b9  sub     rsp, 0x18
8a4bd  mov     rdx, qword ptr [rdi+0x28]
8a4c1  mov     rsi, qword ptr [rdi+0x20]
8a4c5  cmp     rdx, rsi
8a4c8  jbe     0x8a4f3
~~~
### Frame 5: `_IO_file_sync+26`
~~~asm
8a4ca  mov     eax, dword ptr [rdi+0xc0]
8a4d0  test    eax, eax
8a4d2  jle     0x8a550
~~~
### Frame 6: `_IO_file_sync+36`
~~~asm
8a4d4  mov     rax, qword ptr [rdi+0xa0]
8a4db  mov     rsi, qword ptr [rax+0x18]
8a4df  mov     rdx, qword ptr [rax+0x20]
8a4e3  sub     rdx, rsi
8a4e6  sar     rdx, 0x2
8a4ea  call    _IO_wdo_write
~~~
### Frame 7: `_IO_wdo_write`
~~~asm
       _IO_wdo_write:
86220  endbr64 
86224  push    r15
86226  push    r14
86228  push    r13
8622a  push    r12
8622c  push    rbp
8622d  push    rbx
8622e  mov     rbx, rdi
86231  sub     rsp, 0x58
86235  mov     r12, qword ptr [rdi+0x98]
8623c  mov     rax, qword ptr  fs:[0x28]
86245  mov     qword ptr [rsp+0x48], rax
8624a  xor     eax, eax
8624c  test    rdx, rdx
8624f  je      0x86340
~~~
### Frame 8: `_IO_wdo_write+53`
~~~asm
86255  mov     r9, qword ptr [rdi+0x28]
86259  mov     r14, qword ptr [rdi+0x20]
8625d  mov     rbp, rsi
86260  mov     r13, rdx
86263  cmp     qword ptr [rdi+0x30], r9
86267  je      0x863a0
~~~
### Frame 9: `_IO_wdo_write+77`
~~~asm
8626d  lea     rax, [rsp+0x28]
86272  lea     r8, [rsp+0x20]
86277  mov     qword ptr [rsp+errno], rax
8627c  lea     rax, [rsp+0x30]
86281  mov     qword ptr [rsp+0x18], rax
86286  jmp     0x8631e
~~~
### Frame 10: `_IO_wdo_write+254`
~~~asm
8631e  mov     rax, r9
86321  sub     rax, r14
86324  cmp     rax, 0xf
86328  ja      0x86290
~~~
### Frame 11: `_IO_wdo_write+112`
~~~asm
86290  mov     rax, qword ptr [rbx+__libc_dlerror_result]
86294  mov     qword ptr [rsp+0x28], r9
86299  mov     rdi, qword ptr [rbx+0xa0]
862a0  mov     rdx, rbp
862a3  lea     rcx, [rbp+r13*0x4]
862a8  push    qword ptr [rsp+errno]
862ac  push    rax
862ad  lea     rsi, [rdi+0x58]
862b1  mov     rdi, r12
862b4  mov     qword ptr [rsp+0x18], r8
862b9  call    0x86c80
~~~
### Frame 12: `__libio_codecvt_out`
~~~asm
86c80  endbr64 
86c84  push    r15
86c86  movq    xmm0, r9
86c8b  mov     r10, rsi
86c8e  mov     r15, rcx
86c91  push    r14
86c93  lea     rsi, [rdi+__libc_dlerror_result]
86c97  push    r13
86c99  push    r12
86c9b  mov     r12, r8
86c9e  push    rbp
86c9f  push    rbx
86ca0  mov     rbx, rdi
86ca3  sub     rsp, 0x38
86ca7  mov     r13, qword ptr [rdi+0x38]
86cab  mov     rax, qword ptr  fs:[0x28]
86cb4  mov     qword ptr [rsp+0x28], rax
86cb9  xor     eax, eax
86cbb  movhps  xmm0, qword ptr [rsp+0x70]
86cc0  mov     qword ptr [rdi+0x60], r10
86cc4  mov     r14, qword ptr [rsp+0x78]
86cc9  cmp     qword ptr [r13], GLIBC_PRIVATE
86cce  mov     rbp, qword ptr [r13+0x28]
86cd2  mov     qword ptr [rsp+0x20], rdx
86cd7  movups  xmmword ptr [rdi+__libc_dlerror_result], xmm0
86cdb  je      0x86cea
~~~
### Frame 13: `__libio_codecvt_out+106`
~~~asm
86cea  mov     rdi, rbp
86ced  mov     qword ptr [rsp+__resp], rsi
86cf2  call    _dl_mcount_wrapper_check
~~~
### Frame 14: `_dl_mcount_wrapper_check`
~~~asm
        _dl_mcount_wrapper_check:
1754d0  endbr64 
1754d4  mov     rax, qword ptr [0x218fa0]
1754db  mov     rsi, rdi
1754de  cmp     qword ptr [rax+0xa90], GLIBC_PRIVATE
1754e6  je      0x175500
~~~
### Frame 15: `_dl_mcount_wrapper_check+48`
~~~asm
175500  ret     
~~~
### Frame 16: `__libio_codecvt_out+119`
~~~asm
86cf7  lea     rdx, [rsp+0x20]
86cfc  push    GLIBC_PRIVATE
86cfe  mov     rcx, r15
86d01  push    GLIBC_PRIVATE
86d03  xor     r8d, r8d
86d06  mov     rsi, qword ptr [rsp+0x18]
86d0b  mov     rdi, r13
86d0e  lea     r9, [rsp+0x28]
86d13  call    rbp
~~~
--------------------
Call stack:
- `_IO_file_setbuf_mmap`
  - `_IO_file_setbuf`
    - `_IO_default_setbuf`
      - `_IO_file_sync`
        - `_IO_wdo_write`
          - `__libio_codecvt_out`
            - `[_codecvt->__cd_out[63:0] + 0x28]`
--------------------
Conditions:
~~~cpp
_IO_write_ptr > _IO_write_base
_mode >s 0x0
_wide_data->_IO_write_ptr + 0xffffffffffffffff * _wide_data->_IO_write_base >> 0x2 != 0x0
_IO_write_end != _IO_write_ptr
_IO_write_ptr - _IO_write_base > 0xf
[_codecvt->__cd_out[63:0]] == 0x0
~~~
--------------------
Register values at the call:
- `rax`: 0x33a040
- `rcx`: _wide_data->_IO_write_base + (_wide_data->_IO_write_ptr + 0xffffffffffffffff * _wide_data->_IO_write_base >> 0x2[61:0] .. 0)
- `rdx`: 0x7fffffffffefe90
- `rbx`: _codecvt
- `rsp`: 0x7fffffffffefe58
- `rbp`: [_codecvt->__cd_out[63:0] + 0x28]
- `rsi`: 0x40 + _codecvt
- `rdi`: _codecvt->__cd_out[63:0]
- `r8`: 0x0
- `r9`: 0x7fffffffffefe88
- `r10`: 0x58 + _wide_data
- `r11`: orig_r11
- `r12`: 0x7fffffffffeff10
- `r13`: _codecvt->__cd_out[63:0]
- `r14`: 0x7fffffffffeff18
- `r15`: _wide_data->_IO_write_base + (_wide_data->_IO_write_ptr + 0xffffffffffffffff * _wide_data->_IO_write_base >> 0x2[61:0] .. 0)
- `rip`: [_codecvt->__cd_out[63:0] + 0x28]
------------------------------
