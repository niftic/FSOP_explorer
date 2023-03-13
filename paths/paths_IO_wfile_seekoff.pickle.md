# _IO_wfile_seekoff.pickle
234 states with [6, 7, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23] frames
## State 0 with ending 0x83d55
### Frame 0: `_IO_wfile_seekoff`
~~~asm
       _IO_wfile_seekoff:
857d0  endbr64 
857d4  push    r15
857d6  mov     r15, rdi
857d9  push    r14
857db  push    r13
857dd  push    r12
857df  push    rbp
857e0  push    rbx
857e1  sub     rsp, 0xd8
857e8  mov     rax, qword ptr  fs:[0x28]
857f1  mov     qword ptr [rsp+0xc8], rax
857f9  mov     rax, qword ptr [rdi+0xa0]
85800  test    ecx, ecx
85802  je      0x85c08
~~~
### Frame 1: `_IO_wfile_seekoff+56`
~~~asm
85808  mov     r12d, edx
8580b  mov     rcx, qword ptr [rax+0x18]
8580f  mov     rdx, qword ptr [rax+0x20]
85813  mov     rbp, rsi
85816  mov     rbx, qword ptr [rax+__resp]
8581a  cmp     qword ptr [rax+errno], rbx
8581e  je      0x85a70
~~~
### Frame 2: `_IO_wfile_seekoff+84`
~~~asm
85824  mov     dword ptr [rsp+__resp], GLIBC_PRIVATE
8582c  cmp     rcx, rdx
8582f  jae     0x85a88
~~~
### Frame 3: `_IO_wfile_seekoff+101`
~~~asm
85835  mov     rdi, r15
85838  call    _IO_switch_to_wget_mode
~~~
### Frame 4: `_IO_switch_to_wget_mode`
~~~asm
       _IO_switch_to_wget_mode:
83d30  endbr64 
83d34  mov     rax, qword ptr [rdi+0xa0]
83d3b  push    rbx
83d3c  mov     rbx, rdi
83d3f  mov     rdx, qword ptr [rax+0x20]
83d43  cmp     rdx, qword ptr [rax+0x18]
83d47  jbe     0x83d68
~~~
### Frame 5: `_IO_switch_to_wget_mode+25`
~~~asm
83d49  mov     rax, qword ptr [rax+0xe0]
83d50  mov     esi, 0xffffffff
83d55  call    qword ptr [rax+0x18]
~~~
--------------------
Call stack:
- `_IO_wfile_seekoff`
  - `_IO_switch_to_wget_mode`
    - `[_wide_data->_wide_vtable + 0x18]`
--------------------
Conditions:
~~~cpp
orig_rcx[31:0] != 0x0
_wide_data->_IO_read_base != _wide_data->_IO_read_end
_wide_data->_IO_write_base < _wide_data->_IO_write_ptr
_wide_data->_IO_write_ptr > _wide_data->_IO_write_base
~~~
--------------------
Register values at the call:
- `rax`: _wide_data->_wide_vtable
- `rcx`: _wide_data->_IO_write_base
- `rdx`: _wide_data->_IO_write_ptr
- `rbx`: fp
- `rsp`: 0x7fffffffffefed8
- `rbp`: orig_rsi
- `rsi`: 0xffffffff
- `rdi`: fp
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: 0x0 .. orig_rdx[31:0]
- `r13`: orig_r13
- `r14`: orig_r14
- `r15`: fp
- `rip`: [_wide_data->_wide_vtable + 0x18]
------------------------------
## State 2 with ending 0x175500
### Frame 0: `_IO_wfile_seekoff`
~~~asm
       _IO_wfile_seekoff:
857d0  endbr64 
857d4  push    r15
857d6  mov     r15, rdi
857d9  push    r14
857db  push    r13
857dd  push    r12
857df  push    rbp
857e0  push    rbx
857e1  sub     rsp, 0xd8
857e8  mov     rax, qword ptr  fs:[0x28]
857f1  mov     qword ptr [rsp+0xc8], rax
857f9  mov     rax, qword ptr [rdi+0xa0]
85800  test    ecx, ecx
85802  je      0x85c08
~~~
### Frame 1: `_IO_wfile_seekoff+1080`
~~~asm
85c08  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
85c0d  je      0x85db0
~~~
### Frame 2: `_IO_wfile_seekoff+1091`
~~~asm
85c13  mov     edx, dword ptr [rdi]
85c15  mov     rbp, qword ptr [rax+0x20]
85c19  mov     rbx, qword ptr [rax+0x18]
85c1d  mov     edi, edx
85c1f  and     edi, 0x1000
85c25  mov     dword ptr [rsp+__resp], edi
85c29  cmp     rbp, rbx
85c2c  jbe     0x85c85
~~~
### Frame 3: `_IO_wfile_seekoff+1205`
~~~asm
85c85  mov     r13, qword ptr [rax]
85c88  mov     r14, qword ptr [rax+__resp]
85c8c  and     dh, 0x1
85c8f  je      0x85dd0
~~~
### Frame 4: `_IO_wfile_seekoff+1536`
~~~asm
85dd0  mov     rax, qword ptr [rax+errno]
85dd4  mov     qword ptr [rsp+errno], rax
85dd9  jmp     0x85ca7
~~~
### Frame 5: `_IO_wfile_seekoff+1239`
~~~asm
85ca7  mov     r12, qword ptr [r15+0x98]
85cae  mov     rdi, r12
85cb1  call    0x86e80
~~~
### Frame 6: `__libio_codecvt_encoding`
~~~asm
86e80  endbr64 
86e84  mov     rdx, qword ptr [rdi]
86e87  mov     ecx, dword ptr [rdx+0x58]
86e8a  test    ecx, ecx
86e8c  jne     0x86ea0
~~~
### Frame 7: `__libio_codecvt_encoding+14`
~~~asm
86e8e  mov     eax, dword ptr [rdx+0x4c]
86e91  cmp     dword ptr [rdx+0x48], eax
86e94  cmovne  eax, ecx
86e97  ret     
~~~
### Frame 8: `_IO_wfile_seekoff+1254`
~~~asm
85cb6  movsxd  rdx, eax
85cb9  cmp     rbp, rbx
85cbc  ja      0x85de0
~~~
### Frame 9: `_IO_wfile_seekoff+1266`
~~~asm
85cc2  mov     rcx, qword ptr [r15+errno]
85cc6  test    edx, edx
85cc8  jle     0x85ff0
~~~
### Frame 10: `_IO_wfile_seekoff+2080`
~~~asm
85ff0  mov     rdx, qword ptr [r15+0x18]
85ff4  mov     r8, r13
85ff7  sub     r8, qword ptr [rsp+errno]
85ffc  mov     rdi, r12
85fff  mov     rax, qword ptr [r15+0xa0]
86006  lea     rsi, [rsp+0x30]
8600b  sar     r8, 0x2
8600f  mov     rax, qword ptr [rax+0x60]
86013  mov     qword ptr [rsp+0x30], rax
86018  call    0x86eb0
~~~
### Frame 11: `__libio_codecvt_length`
~~~asm
86eb0  endbr64 
86eb4  push    rbp
86eb5  shl     r8, 0x2
86eb9  mov     rbp, rsp
86ebc  push    r15
86ebe  push    r14
86ec0  mov     r14, rcx
86ec3  push    r13
86ec5  push    r12
86ec7  mov     r12, rdx
86eca  push    rbx
86ecb  sub     rsp, 0x28
86ecf  mov     rax, qword ptr  fs:[0x28]
86ed8  mov     qword ptr [rbp-0x38], rax
86edc  xor     eax, eax
86ede  lea     rax, [r8+0xf]
86ee2  mov     qword ptr [rbp-0x48], rdx
86ee6  mov     rcx, rsp
86ee9  mov     rdx, rax
86eec  and     rax, 0xfffffffffffff000
86ef2  sub     rcx, rax
86ef5  and     rdx, 0xfffffffffffffff0
86ef9  cmp     rsp, rcx
86efc  je      0x86f13
~~~
### Frame 12: `__libio_codecvt_length+99`
~~~asm
86f13  and     edx, 0xfff
86f19  sub     rsp, rdx
86f1c  test    rdx, rdx
86f1f  jne     0x86fa8
~~~
### Frame 13: `__libio_codecvt_length+117`
~~~asm
86f25  mov     rax, rsp
86f28  mov     r15, qword ptr [rdi]
86f2b  mov     qword ptr [rdi+0x28], rsi
86f2f  lea     r13, [rdi+__resp]
86f33  add     r8, rax
86f36  movq    xmm0, rax
86f3b  movq    xmm1, r8
86f40  cmp     qword ptr [r15], GLIBC_PRIVATE
86f44  mov     rbx, qword ptr [r15+0x28]
86f48  punpcklqdq xmm0, xmm1
86f4c  movups  xmmword ptr [rdi+__resp], xmm0
86f50  je      0x86f5f
~~~
### Frame 14: `__libio_codecvt_length+175`
~~~asm
86f5f  mov     rdi, rbx
86f62  call    _dl_mcount_wrapper_check
~~~
### Frame 15: `_dl_mcount_wrapper_check`
~~~asm
        _dl_mcount_wrapper_check:
1754d0  endbr64 
1754d4  mov     rax, qword ptr [0x218fa0]
1754db  mov     rsi, rdi
1754de  cmp     qword ptr [rax+0xa90], GLIBC_PRIVATE
1754e6  je      0x175500
~~~
### Frame 16: `_dl_mcount_wrapper_check+48`
~~~asm
175500  ret     
~~~
--------------------
Call stack:
- `_IO_wfile_seekoff`
  - `__libio_codecvt_length`
    - `_dl_mcount_wrapper_check`
      - `[0x7fffffffffefe88 + 0xffffffffffffffff * (0x0 .. 0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[11:4] .. 0)]`
--------------------
Conditions:
~~~cpp
orig_rcx[31:0] == 0x0
_wide_data->_IO_buf_base != 0x0
_wide_data->_IO_write_ptr <= _wide_data->_IO_write_base
(_flags[15:8] & 1) == 0
[_codecvt->__cd_in[63:0] + 0x58][31:0] == 0x0
_wide_data->_IO_write_ptr <= _wide_data->_IO_write_base
(if [_codecvt->__cd_in[63:0] + 0x48][31:0] == [_codecvt->__cd_in[63:0] + 0x4c][31:0] then [_codecvt->__cd_in[63:0] + 0x4c][31:0] else [_codecvt->__cd_in[63:0] + 0x58][31:0]) <=s 0x0
0x7fffffffffefe90 - ((_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2 << 0x2) + 0xf & 0xfffffffffffff000) == 0x7fffffffffefe90
((0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[15:4] .. 0) & 0xfff) == 0x0
[_codecvt->__cd_in[63:0]] == 0x0
~~~
--------------------
Register values at the call:
- `rax`: 0x33a040
- `rcx`: 0x7fffffffffefe90 + 0xffffffffffffffff * (0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[63:12] .. 0x0)
- `rdx`: 0x0 .. 0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[11:4] .. 0
- `rbx`: [_codecvt->__cd_in[63:0] + 0x28]
- `rsp`: 0x7fffffffffefe90 + 0xffffffffffffffff * (0x0 .. 0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[11:4] .. 0)
- `rbp`: 0x7fffffffffefee0
- `rsi`: [_codecvt->__cd_in[63:0] + 0x28]
- `rdi`: [_codecvt->__cd_in[63:0] + 0x28]
- `r8`: 0x7fffffffffefe90 + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0) + 0xffffffffffffffff * (0x0 .. 0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[11:4] .. 0)
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: _IO_read_base
- `r13`: 0x8 + _codecvt
- `r14`: _IO_read_end
- `r15`: _codecvt->__cd_in[63:0]
- `rip`: [0x7fffffffffefe88 + 0xffffffffffffffff * (0x0 .. 0xf + (_wide_data->_IO_read_ptr + 0xffffffffffffffff * _wide_data->_IO_read_base >> 0x2[61:0] .. 0)[11:4] .. 0)]
------------------------------
## State 22 with ending 0x86f7f
### Frame 0: `_IO_wfile_seekoff`
~~~asm
       _IO_wfile_seekoff:
857d0  endbr64 
857d4  push    r15
857d6  mov     r15, rdi
857d9  push    r14
857db  push    r13
857dd  push    r12
857df  push    rbp
857e0  push    rbx
857e1  sub     rsp, 0xd8
857e8  mov     rax, qword ptr  fs:[0x28]
857f1  mov     qword ptr [rsp+0xc8], rax
857f9  mov     rax, qword ptr [rdi+0xa0]
85800  test    ecx, ecx
85802  je      0x85c08
~~~
### Frame 1: `_IO_wfile_seekoff+1080`
~~~asm
85c08  cmp     qword ptr [rax+0x30], GLIBC_PRIVATE
85c0d  je      0x85db0
~~~
### Frame 2: `_IO_wfile_seekoff+1091`
~~~asm
85c13  mov     edx, dword ptr [rdi]
85c15  mov     rbp, qword ptr [rax+0x20]
85c19  mov     rbx, qword ptr [rax+0x18]
85c1d  mov     edi, edx
85c1f  and     edi, 0x1000
85c25  mov     dword ptr [rsp+__resp], edi
85c29  cmp     rbp, rbx
85c2c  jbe     0x85c85
~~~
### Frame 3: `_IO_wfile_seekoff+1205`
~~~asm
85c85  mov     r13, qword ptr [rax]
85c88  mov     r14, qword ptr [rax+__resp]
85c8c  and     dh, 0x1
85c8f  je      0x85dd0
~~~
### Frame 4: `_IO_wfile_seekoff+1221`
~~~asm
85c95  cmp     r14, r13
85c98  ja      0x85d03
~~~
### Frame 5: `_IO_wfile_seekoff+1226`
~~~asm
85c9a  mov     r13, qword ptr [rax+__libc_dlerror_result]
85c9e  mov     r14, qword ptr [rax+0x50]
85ca2  mov     qword ptr [rsp+errno], r13
85ca7  mov     r12, qword ptr [r15+0x98]
85cae  mov     rdi, r12
85cb1  call    0x86e80
~~~
### Frame 6: `__libio_codecvt_encoding`
~~~asm
86e80  endbr64 
86e84  mov     rdx, qword ptr [rdi]
86e87  mov     ecx, dword ptr [rdx+0x58]
86e8a  test    ecx, ecx
86e8c  jne     0x86ea0
~~~
### Frame 7: `__libio_codecvt_encoding+14`
~~~asm
86e8e  mov     eax, dword ptr [rdx+0x4c]
86e91  cmp     dword ptr [rdx+0x48], eax
86e94  cmovne  eax, ecx
86e97  ret     
~~~
### Frame 8: `_IO_wfile_seekoff+1254`
~~~asm
85cb6  movsxd  rdx, eax
85cb9  cmp     rbp, rbx
85cbc  ja      0x85de0
~~~
### Frame 9: `_IO_wfile_seekoff+1266`
~~~asm
85cc2  mov     rcx, qword ptr [r15+errno]
85cc6  test    edx, edx
85cc8  jle     0x85ff0
~~~
### Frame 10: `_IO_wfile_seekoff+2080`
~~~asm
85ff0  mov     rdx, qword ptr [r15+0x18]
85ff4  mov     r8, r13
85ff7  sub     r8, qword ptr [rsp+errno]
85ffc  mov     rdi, r12
85fff  mov     rax, qword ptr [r15+0xa0]
86006  lea     rsi, [rsp+0x30]
8600b  sar     r8, 0x2
8600f  mov     rax, qword ptr [rax+0x60]
86013  mov     qword ptr [rsp+0x30], rax
86018  call    0x86eb0
~~~
### Frame 11: `__libio_codecvt_length`
~~~asm
86eb0  endbr64 
86eb4  push    rbp
86eb5  shl     r8, 0x2
86eb9  mov     rbp, rsp
86ebc  push    r15
86ebe  push    r14
86ec0  mov     r14, rcx
86ec3  push    r13
86ec5  push    r12
86ec7  mov     r12, rdx
86eca  push    rbx
86ecb  sub     rsp, 0x28
86ecf  mov     rax, qword ptr  fs:[0x28]
86ed8  mov     qword ptr [rbp-0x38], rax
86edc  xor     eax, eax
86ede  lea     rax, [r8+0xf]
86ee2  mov     qword ptr [rbp-0x48], rdx
86ee6  mov     rcx, rsp
86ee9  mov     rdx, rax
86eec  and     rax, 0xfffffffffffff000
86ef2  sub     rcx, rax
86ef5  and     rdx, 0xfffffffffffffff0
86ef9  cmp     rsp, rcx
86efc  je      0x86f13
~~~
### Frame 12: `__libio_codecvt_length+99`
~~~asm
86f13  and     edx, 0xfff
86f19  sub     rsp, rdx
86f1c  test    rdx, rdx
86f1f  jne     0x86fa8
~~~
### Frame 13: `__libio_codecvt_length+117`
~~~asm
86f25  mov     rax, rsp
86f28  mov     r15, qword ptr [rdi]
86f2b  mov     qword ptr [rdi+0x28], rsi
86f2f  lea     r13, [rdi+__resp]
86f33  add     r8, rax
86f36  movq    xmm0, rax
86f3b  movq    xmm1, r8
86f40  cmp     qword ptr [r15], GLIBC_PRIVATE
86f44  mov     rbx, qword ptr [r15+0x28]
86f48  punpcklqdq xmm0, xmm1
86f4c  movups  xmmword ptr [rdi+__resp], xmm0
86f50  je      0x86f5f
~~~
### Frame 14: `__libio_codecvt_length+175`
~~~asm
86f5f  mov     rdi, rbx
86f62  call    _dl_mcount_wrapper_check
~~~
### Frame 15: `_dl_mcount_wrapper_check`
~~~asm
        _dl_mcount_wrapper_check:
1754d0  endbr64 
1754d4  mov     rax, qword ptr [0x218fa0]
1754db  mov     rsi, rdi
1754de  cmp     qword ptr [rax+0xa90], GLIBC_PRIVATE
1754e6  je      0x175500
~~~
### Frame 16: `_dl_mcount_wrapper_check+48`
~~~asm
175500  ret     
~~~
### Frame 17: `__libio_codecvt_length+183`
~~~asm
86f67  push    GLIBC_PRIVATE
86f69  lea     rdx, [rbp-0x48]
86f6d  lea     r9, [rbp-0x40]
86f71  push    GLIBC_PRIVATE
86f73  xor     r8d, r8d
86f76  mov     rcx, r14
86f79  mov     rsi, r13
86f7c  mov     rdi, r15
86f7f  call    rbx
~~~
--------------------
Call stack:
- `_IO_wfile_seekoff`
  - `__libio_codecvt_length`
    - `[_codecvt->__cd_in[63:0] + 0x28]`
--------------------
Conditions:
~~~cpp
orig_rcx[31:0] == 0x0
_wide_data->_IO_buf_base != 0x0
_wide_data->_IO_write_ptr <= _wide_data->_IO_write_base
(_flags[15:8] & 1) != 0
_wide_data->_IO_read_end <= _wide_data->_IO_read_ptr
[_codecvt->__cd_in[63:0] + 0x58][31:0] == 0x0
_wide_data->_IO_write_ptr <= _wide_data->_IO_write_base
(if [_codecvt->__cd_in[63:0] + 0x48][31:0] == [_codecvt->__cd_in[63:0] + 0x4c][31:0] then [_codecvt->__cd_in[63:0] + 0x4c][31:0] else [_codecvt->__cd_in[63:0] + 0x58][31:0]) <=s 0x0
[_codecvt->__cd_in[63:0]] == 0x0
~~~
--------------------
Register values at the call:
- `rax`: 0x33a040
- `rcx`: _IO_read_end
- `rdx`: 0x7fffffffffefe98
- `rbx`: [_codecvt->__cd_in[63:0] + 0x28]
- `rsp`: 0x7fffffffffefe78
- `rbp`: 0x7fffffffffefee0
- `rsi`: 0x8 + _codecvt
- `rdi`: _codecvt->__cd_in[63:0]
- `r8`: 0x0
- `r9`: 0x7fffffffffefea0
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: _IO_read_base
- `r13`: 0x8 + _codecvt
- `r14`: _IO_read_end
- `r15`: _codecvt->__cd_in[63:0]
- `rip`: [_codecvt->__cd_in[63:0] + 0x28]
------------------------------
