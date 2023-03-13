# _IO_obstack_overflow.pickle
2 states with [5, 5] frames
## State 0 with ending 0xa78c3
### Frame 0: `_IO_obstack_overflow`
~~~asm
88650  endbr64 
88654  push    r12
88656  push    rbp
88657  push    rbx
88658  mov     rbx, qword ptr [rdi+0xe0]
8865f  cmp     esi, -0x1
88662  je      0x886c7
~~~
### Frame 1: `_IO_obstack_overflow+20`
~~~asm
88664  mov     rax, qword ptr [rbx+0x18]
88668  mov     rbp, rdi
8866b  mov     r12d, esi
8866e  lea     rdx, [rax+0x1]
88672  cmp     rdx, qword ptr [rbx+0x20]
88676  ja      0x886b0
~~~
### Frame 2: `_IO_obstack_overflow+96`
~~~asm
886b0  mov     esi, 0x1
886b5  mov     rdi, rbx
886b8  call    _obstack_newchunk
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
- `_IO_obstack_overflow`
  - `_obstack_newchunk`
    - `[next_FILE + 0x38]`
--------------------
Conditions:
~~~cpp
orig_rsi[31:0] != 0xffffffff
[next_FILE + 0x18] + 0x1 > [next_FILE + 0x20]
([next_FILE + 0x50][7:0] & 1) == 0
~~~
--------------------
Register values at the call:
- `rax`: [next_FILE + 0x38]
- `rcx`: orig_rcx
- `rdx`: [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]
- `rbx`: next_FILE
- `rsp`: 0x7fffffffffeffa8
- `rbp`: [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10]
- `rsi`: 0x1
- `rdi`: if [next_FILE] <=s 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: if [next_FILE] <=s 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r13`: orig_r13
- `r14`: [next_FILE + 0x8]
- `r15`: orig_r15
- `rip`: [next_FILE + 0x38]
------------------------------
## State 1 with ending 0xa7753
### Frame 0: `_IO_obstack_overflow`
~~~asm
88650  endbr64 
88654  push    r12
88656  push    rbp
88657  push    rbx
88658  mov     rbx, qword ptr [rdi+0xe0]
8865f  cmp     esi, -0x1
88662  je      0x886c7
~~~
### Frame 1: `_IO_obstack_overflow+20`
~~~asm
88664  mov     rax, qword ptr [rbx+0x18]
88668  mov     rbp, rdi
8866b  mov     r12d, esi
8866e  lea     rdx, [rax+0x1]
88672  cmp     rdx, qword ptr [rbx+0x20]
88676  ja      0x886b0
~~~
### Frame 2: `_IO_obstack_overflow+96`
~~~asm
886b0  mov     esi, 0x1
886b5  mov     rdi, rbx
886b8  call    _obstack_newchunk
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
- `_IO_obstack_overflow`
  - `_obstack_newchunk`
    - `[next_FILE + 0x38]`
--------------------
Conditions:
~~~cpp
orig_rsi[31:0] != 0xffffffff
[next_FILE + 0x18] + 0x1 > [next_FILE + 0x20]
([next_FILE + 0x50][7:0] & 1) != 0
~~~
--------------------
Register values at the call:
- `rax`: [next_FILE + 0x38]
- `rcx`: orig_rcx
- `rdx`: [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]
- `rbx`: next_FILE
- `rsp`: 0x7fffffffffeffa8
- `rbp`: [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10]
- `rsi`: if [next_FILE] <=s 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `rdi`: [next_FILE + 0x48]
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: if [next_FILE] <=s 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) then 0x65 + [next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] + ([next_FILE + 0x18] + 0xffffffffffffffff * [next_FILE + 0x10] >> 0x3) + ([next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:31] .. [next_FILE + 0x30][31:0]) else [next_FILE]
- `r13`: orig_r13
- `r14`: [next_FILE + 0x8]
- `r15`: orig_r15
- `rip`: [next_FILE + 0x38]
------------------------------
