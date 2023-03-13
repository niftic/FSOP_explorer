# _IO_obstack_xsputn.pickle
2 states with [5, 5] frames
## State 0 with ending 0xa78c3
### Frame 0: `_IO_obstack_xsputn`
~~~asm
88590  endbr64 
88594  push    r14
88596  mov     r14, rsi
88599  push    r13
8859b  push    r12
8859d  mov     r12, rdx
885a0  push    rbp
885a1  push    rbx
885a2  mov     rbx, rdi
885a5  mov     r13, qword ptr [rdi+0xe0]
885ac  mov     rdi, qword ptr [rdi+0x28]
885b0  mov     rax, qword ptr [rbx+0x30]
885b4  add     rdx, rdi
885b7  cmp     rax, rdx
885ba  jae     0x88630
~~~
### Frame 1: `_IO_obstack_xsputn+44`
~~~asm
885bc  sub     rdi, rax
885bf  movsxd  rbp, r12d
885c2  add     rdi, qword ptr [r13+0x18]
885c6  mov     esi, r12d
885c9  mov     qword ptr [r13+0x18], rdi
885cd  lea     rax, [rdi+rbp]
885d1  cmp     qword ptr [r13+0x20], rax
885d5  jb      0x88620
~~~
### Frame 2: `_IO_obstack_xsputn+144`
~~~asm
88620  mov     rdi, r13
88623  call    _obstack_newchunk
~~~
### Frame 3: `_obstack_newchunk`
~~~asm
       _obstack_newchunk:
a7700  endbr64 
a7704  push    r14
a7706  movsxd  rax, esi
a7709  push    r13
a770b  push    r12
a770d  push    rbp
a770e  push    rbx
a770f  mov     rbp, qword ptr [rdi+0x18]
a7713  mov     rbx, rdi
a7716  sub     rbp, qword ptr [rdi+errno]
a771a  mov     r14, qword ptr [rdi+__resp]
a771e  mov     rdx, rbp
a7721  add     rax, rbp
a7724  sar     rdx, 0x3
a7728  add     rax, rdx
a772b  movsxd  rdx, dword ptr [rdi+0x30]
a772f  lea     r12, [rax+rdx+0x64]
a7734  mov     rax, qword ptr [rdi]
a7737  cmp     r12, rax
a773a  cmovl   r12, rax
a773e  mov     rax, qword ptr [rdi+0x38]
a7742  test    byte ptr [rdi+0x50], 0x1
a7746  je      0xa78c0
~~~
### Frame 4: `_obstack_newchunk+448`
~~~asm
a78c0  mov     rdi, r12
a78c3  call    rax
~~~
--------------------
Call stack:
- `_IO_obstack_xsputn`
  - `_obstack_newchunk`
    - `[next_FILE + 0x38]`
--------------------
Conditions:
~~~cpp
_IO_write_end < orig_rdx + _IO_write_ptr
[next_FILE + 0x20] < _IO_write_ptr - _IO_write_end + [next_FILE + 0x18] + SignExt(32, orig_rdx[31:0])
([next_FILE + 0x50][7:0] & 1) == 0
~~~
--------------------
Register values at the call:
- `rax`: [next_FILE + 0x38]
- `rcx`: orig_rcx
- `rdx`: [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]
- `rbx`: next_FILE
- `rsp`: 0x7fffffffffeff98
- `rbp`: _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10]
- `rsi`: 0x0 .. orig_rdx[31:0]
- `rdi`: if [next_FILE] <=s 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: if [next_FILE] <=s 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r13`: next_FILE
- `r14`: [next_FILE + 0x8]
- `r15`: orig_r15
- `rip`: [next_FILE + 0x38]
------------------------------
## State 1 with ending 0xa7753
### Frame 0: `_IO_obstack_xsputn`
~~~asm
88590  endbr64 
88594  push    r14
88596  mov     r14, rsi
88599  push    r13
8859b  push    r12
8859d  mov     r12, rdx
885a0  push    rbp
885a1  push    rbx
885a2  mov     rbx, rdi
885a5  mov     r13, qword ptr [rdi+0xe0]
885ac  mov     rdi, qword ptr [rdi+0x28]
885b0  mov     rax, qword ptr [rbx+0x30]
885b4  add     rdx, rdi
885b7  cmp     rax, rdx
885ba  jae     0x88630
~~~
### Frame 1: `_IO_obstack_xsputn+44`
~~~asm
885bc  sub     rdi, rax
885bf  movsxd  rbp, r12d
885c2  add     rdi, qword ptr [r13+0x18]
885c6  mov     esi, r12d
885c9  mov     qword ptr [r13+0x18], rdi
885cd  lea     rax, [rdi+rbp]
885d1  cmp     qword ptr [r13+0x20], rax
885d5  jb      0x88620
~~~
### Frame 2: `_IO_obstack_xsputn+144`
~~~asm
88620  mov     rdi, r13
88623  call    _obstack_newchunk
~~~
### Frame 3: `_obstack_newchunk`
~~~asm
       _obstack_newchunk:
a7700  endbr64 
a7704  push    r14
a7706  movsxd  rax, esi
a7709  push    r13
a770b  push    r12
a770d  push    rbp
a770e  push    rbx
a770f  mov     rbp, qword ptr [rdi+0x18]
a7713  mov     rbx, rdi
a7716  sub     rbp, qword ptr [rdi+errno]
a771a  mov     r14, qword ptr [rdi+__resp]
a771e  mov     rdx, rbp
a7721  add     rax, rbp
a7724  sar     rdx, 0x3
a7728  add     rax, rdx
a772b  movsxd  rdx, dword ptr [rdi+0x30]
a772f  lea     r12, [rax+rdx+0x64]
a7734  mov     rax, qword ptr [rdi]
a7737  cmp     r12, rax
a773a  cmovl   r12, rax
a773e  mov     rax, qword ptr [rdi+0x38]
a7742  test    byte ptr [rdi+0x50], 0x1
a7746  je      0xa78c0
~~~
### Frame 4: `_obstack_newchunk+76`
~~~asm
a774c  mov     rdi, qword ptr [rdi+0x48]
a7750  mov     rsi, r12
a7753  call    rax
~~~
--------------------
Call stack:
- `_IO_obstack_xsputn`
  - `_obstack_newchunk`
    - `[next_FILE + 0x38]`
--------------------
Conditions:
~~~cpp
_IO_write_end < orig_rdx + _IO_write_ptr
[next_FILE + 0x20] < _IO_write_ptr - _IO_write_end + [next_FILE + 0x18] + SignExt(32, orig_rdx[31:0])
([next_FILE + 0x50][7:0] & 1) != 0
~~~
--------------------
Register values at the call:
- `rax`: [next_FILE + 0x38]
- `rcx`: orig_rcx
- `rdx`: [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]
- `rbx`: next_FILE
- `rsp`: 0x7fffffffffeff98
- `rbp`: _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10]
- `rsi`: if [next_FILE] <=s 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `rdi`: [next_FILE + 0x48]
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: if [next_FILE] <=s 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x64 + (orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:31] .. orig_rdx[31:0]) + _IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + (_IO_write_ptr + 0xffffffffffffffff * _IO_write_end + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r13`: next_FILE
- `r14`: [next_FILE + 0x8]
- `r15`: orig_r15
- `rip`: [next_FILE + 0x38]
------------------------------
