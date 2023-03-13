# _IO_wdefault_xsgetn.pickle
27 states with [8, 11, 15, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20] frames
## State 0 with ending 0x83d55
### Frame 0: `_IO_wdefault_xsgetn`
~~~asm
       _IO_wdefault_xsgetn:
840b0  endbr64 
840b4  push    r15
840b6  mov     r15, rdi
840b9  push    r14
840bb  lea     r14, [0x215a00]
840c2  push    r13
840c4  lea     r13, [0x216768]
840cb  push    r12
840cd  sub     r13, r14
840d0  mov     r12, rdx
840d3  push    rbp
840d4  mov     rbp, rsi
840d7  push    rbx
840d8  mov     rbx, rdx
840db  sub     rsp, 0x18
840df  nop     
840e0  mov     rdi, qword ptr [r15+0xa0]
840e7  mov     rsi, qword ptr [rdi]
840ea  mov     rax, qword ptr [rdi+__resp]
840ee  sub     rax, rsi
840f1  test    rax, rax
840f4  jle     0x8411b
~~~
### Frame 1: `_IO_wdefault_xsgetn+107`
~~~asm
8411b  test    rbx, rbx
8411e  je      0x841e3
~~~
### Frame 2: `_IO_wdefault_xsgetn+116`
~~~asm
84124  mov     edx, dword ptr [r15+0xc0]
8412b  test    edx, edx
8412d  js      0x841e0
~~~
### Frame 3: `_IO_wdefault_xsgetn+131`
~~~asm
84133  je      0x84200
~~~
### Frame 4: `_IO_wdefault_xsgetn+137`
~~~asm
84139  test    dword ptr [r15], 0x800
84140  jne     0x8423b
~~~
### Frame 5: `_IO_wdefault_xsgetn+395`
~~~asm
8423b  mov     rdi, r15
8423e  call    _IO_switch_to_wget_mode
~~~
### Frame 6: `_IO_switch_to_wget_mode`
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
### Frame 7: `_IO_switch_to_wget_mode+25`
~~~asm
83d49  mov     rax, qword ptr [rax+0xe0]
83d50  mov     esi, 0xffffffff
83d55  call    qword ptr [rax+0x18]
~~~
--------------------
Call stack:
- `_IO_wdefault_xsgetn`
  - `_IO_switch_to_wget_mode`
    - `[_wide_data->_wide_vtable + 0x18]`
--------------------
Conditions:
~~~cpp
(_wide_data->_IO_read_end - _wide_data->_IO_read_ptr[63:63] | (if _wide_data->_IO_read_end - _wide_data->_IO_read_ptr == 0x0 then 1 else 0)) != 0
orig_rdx != 0x0
(LShR((0#32 .. _mode), 0x1f)[0:0] & 1) == 0
_mode != 0x0
(_flags[15:0] & 0x800) != 0x0
_wide_data->_IO_write_ptr > _wide_data->_IO_write_base
~~~
--------------------
Register values at the call:
- `rax`: _wide_data->_wide_vtable
- `rcx`: orig_rcx
- `rdx`: _wide_data->_IO_write_ptr
- `rbx`: fp
- `rsp`: 0x7fffffffffeff98
- `rbp`: orig_rsi
- `rsi`: 0xffffffff
- `rdi`: fp
- `r8`: orig_r8
- `r9`: orig_r9
- `r10`: orig_r10
- `r11`: orig_r11
- `r12`: orig_rdx
- `r13`: 0xd68
- `r14`: 0x215a00
- `r15`: fp
- `rip`: [_wide_data->_wide_vtable + 0x18]
------------------------------
