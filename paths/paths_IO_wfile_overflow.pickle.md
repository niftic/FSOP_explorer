# _IO_wfile_overflow.pickle
71 states with [7, 15, 16, 16, 17, 17, 17, 18, 18, 19, 19, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 26, 27, 28, 28, 29, 30, 31, 32, 32, 32, 33, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 36, 36, 37, 37, 37, 37, 38, 38, 38, 38, 41, 41, 42, 42, 43, 43, 44, 44, 44, 44, 45, 45, 46, 46, 47, 47] frames
## State 0 with ending 0x83c1b
### Frame 0: `_IO_wfile_overflow`
~~~asm
       _IO_wfile_overflow:
86410  endbr64 
86414  push    r12
86416  push    rbp
86417  mov     rbp, rdi
8641a  sub     rsp, __resp
8641e  mov     eax, dword ptr [rdi]
86420  test    al, __resp
86422  jne     0x86540
~~~
### Frame 1: `_IO_wfile_overflow+24`
~~~asm
86428  mov     r12d, esi
8642b  test    ah, __resp
8642e  jne     0x864ac
~~~
### Frame 2: `_IO_wfile_overflow+32`
~~~asm
86430  mov     rdx, qword ptr [rdi+0xa0]
86437  cmp     qword ptr [rdx+0x18], GLIBC_PRIVATE
8643c  je      0x86670
~~~
### Frame 3: `_IO_wfile_overflow+608`
~~~asm
86670  call    _IO_wdoallocbuf
~~~
### Frame 4: `_IO_wdoallocbuf`
~~~asm
       _IO_wdoallocbuf:
83bf0  endbr64 
83bf4  mov     rax, qword ptr [rdi+0xa0]
83bfb  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
83c00  je      0x83c08
~~~
### Frame 5: `_IO_wdoallocbuf+24`
~~~asm
83c08  push    r12
83c0a  push    rbp
83c0b  push    rbx
83c0c  mov     rbx, rdi
83c0f  test    byte ptr [rdi], 0x2
83c12  jne     0x83c88
~~~
### Frame 6: `_IO_wdoallocbuf+36`
~~~asm
83c14  mov     rax, qword ptr [rax+0xe0]
83c1b  call    qword ptr [rax+0x68]
~~~
--------------------
Call stack:
- `_IO_wfile_overflow`
  - `_IO_wdoallocbuf`
    - `[_wide_data->_wide_vtable + 0x68]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 8) == 0
(_flags[15:8] & 8) == 0
_wide_data->_IO_write_base == 0x0
_wide_data->_IO_buf_base == 0x0
(_flags[7:0] & 2) == 0
~~~
--------------------
Register values at the call:
- `rax`: _wide_data->_wide_vtable
- `rcx`: orig_rcx
- `rdx`: _wide_data
- `rbx`: fp
- `rsp`: 0x7fffffffffeffb8
- `rbp`: fp
- `rsi`: orig_rsi
- `rdi`: fp
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: 0x0 .. orig_rsi[31:0]
- `r13`: orig_r13
- `r14`: orig_r14
- `r15`: orig_r15
- `rip`: [_wide_data->_wide_vtable + 0x68]
------------------------------
## State 1 with ending 0x86d13
### Frame 0: `_IO_wfile_overflow`
~~~asm
       _IO_wfile_overflow:
86410  endbr64 
86414  push    r12
86416  push    rbp
86417  mov     rbp, rdi
8641a  sub     rsp, __resp
8641e  mov     eax, dword ptr [rdi]
86420  test    al, __resp
86422  jne     0x86540
~~~
### Frame 1: `_IO_wfile_overflow+24`
~~~asm
86428  mov     r12d, esi
8642b  test    ah, __resp
8642e  jne     0x864ac
~~~
### Frame 2: `_IO_wfile_overflow+156`
~~~asm
864ac  cmp     r12d, -0x1
864b0  je      0x86577
~~~
### Frame 3: `_IO_wfile_overflow+359`
~~~asm
86577  mov     edi, dword ptr [rbp+0xc0]
8657d  test    edi, edi
8657f  jle     0x866c0
~~~
### Frame 4: `_IO_wfile_overflow+373`
~~~asm
86585  mov     rax, qword ptr [rbp+0xa0]
8658c  mov     rdi, rbp
8658f  mov     rsi, qword ptr [rax+0x18]
86593  mov     rdx, qword ptr [rax+0x20]
86597  add     rsp, __resp
8659b  pop     rbp
8659c  pop     r12
8659e  sub     rdx, rsi
865a1  sar     rdx, 0x2
865a5  jmp     _IO_wdo_write
~~~
### Frame 5: `_IO_wfile_overflow+-496`
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
### Frame 6: `_IO_wfile_overflow+-443`
~~~asm
86255  mov     r9, qword ptr [rdi+0x28]
86259  mov     r14, qword ptr [rdi+0x20]
8625d  mov     rbp, rsi
86260  mov     r13, rdx
86263  cmp     qword ptr [rdi+0x30], r9
86267  je      0x863a0
~~~
### Frame 7: `_IO_wfile_overflow+-419`
~~~asm
8626d  lea     rax, [rsp+0x28]
86272  lea     r8, [rsp+0x20]
86277  mov     qword ptr [rsp+errno], rax
8627c  lea     rax, [rsp+0x30]
86281  mov     qword ptr [rsp+0x18], rax
86286  jmp     0x8631e
~~~
### Frame 8: `_IO_wfile_overflow+-242`
~~~asm
8631e  mov     rax, r9
86321  sub     rax, r14
86324  cmp     rax, 0xf
86328  ja      0x86290
~~~
### Frame 9: `_IO_wfile_overflow+-384`
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
### Frame 10: `__libio_codecvt_out`
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
### Frame 11: `__libio_codecvt_out+106`
~~~asm
86cea  mov     rdi, rbp
86ced  mov     qword ptr [rsp+__resp], rsi
86cf2  call    _dl_mcount_wrapper_check
~~~
### Frame 12: `_dl_mcount_wrapper_check`
~~~asm
        _dl_mcount_wrapper_check:
1754d0  endbr64 
1754d4  mov     rax, qword ptr [0x218fa0]
1754db  mov     rsi, rdi
1754de  cmp     qword ptr [rax+0xa90], GLIBC_PRIVATE
1754e6  je      0x175500
~~~
### Frame 13: `_dl_mcount_wrapper_check+48`
~~~asm
175500  ret     
~~~
### Frame 14: `__libio_codecvt_out+119`
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
- `_IO_wfile_overflow`
  - `__libio_codecvt_out`
    - `[_codecvt->__cd_out[63:0] + 0x28]`
--------------------
Conditions:
~~~cpp
(_flags[7:0] & 8) == 0
(_flags[15:8] & 8) != 0
orig_rsi[31:0] == 0xffffffff
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
- `rdx`: 0x7fffffffffeff10
- `rbx`: _codecvt
- `rsp`: 0x7fffffffffefed8
- `rbp`: [_codecvt->__cd_out[63:0] + 0x28]
- `rsi`: 0x40 + _codecvt
- `rdi`: _codecvt->__cd_out[63:0]
- `r8`: 0x0
- `r9`: 0x7fffffffffeff08
- `r10`: 0x58 + _wide_data
- `r11`: orig_r11
- `r12`: 0x7fffffffffeff90
- `r13`: _codecvt->__cd_out[63:0]
- `r14`: 0x7fffffffffeff98
- `r15`: _wide_data->_IO_write_base + (_wide_data->_IO_write_ptr + 0xffffffffffffffff * _wide_data->_IO_write_base >> 0x2[61:0] .. 0)
- `rip`: [_codecvt->__cd_out[63:0] + 0x28]
------------------------------
