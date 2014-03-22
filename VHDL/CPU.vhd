----------------------------------------------------------------------------------
-- Company: 
-- Engineer: Nick LaRosa
-- 
-- Create Date:    17:25:37 12/31/2013 
-- Design Name: 
-- Module Name:    CPU - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity CPU is
Generic (     data_width : integer := 16;
              inst_width : integer := 16;
          RAM_addr_width : integer := 16;
          ROM_addr_width : integer := 16
        );

Port (        inM : in std_logic_vector(data_width - 1 downto 0);
      instruction : in std_logic_vector(inst_width - 1 downto 0);
            reset : in std_logic;
            
           writeM : out std_logic;
             outM : out std_logic_vector(data_width - 1 downto 0);
         addressM : out std_logic_vector(RAM_addr_width - 1 downto 0);
               pc : out std_logic_vector(ROM_addr_width - 1 downto 0)
      );
end CPU;

architecture Behavioral of CPU is

begin


end Behavioral;

