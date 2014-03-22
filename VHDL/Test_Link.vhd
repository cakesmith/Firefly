--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   15:54:23 12/31/2013
-- Design Name:   
-- Module Name:   /home/nick/Jarvis/Test_Link.vhd
-- Project Name:  Jarvis
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: Link
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
USE ieee.numeric_std.ALL;
 
ENTITY Test_Link IS
END Test_Link;
 
ARCHITECTURE behavior OF Test_Link IS 
 
    constant nodes : integer := 5;
    constant c_addr_width : positive := 32;
    constant c_data_width : positive := 32;
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT Link
    
    generic ( addr_width : positive := c_addr_width;
              data_width : positive := c_data_width;
              num_cells : positive
             );
             
    PORT(
         in_address : IN  std_logic_vector(31 downto 0);
         in_data : IN  std_logic_vector(31 downto 0);
         in_wr : IN  std_logic;
         out_address : OUT  std_logic_vector(31 downto 0);
         out_data : OUT  std_logic_vector(31 downto 0);
         out_wr : OUT  std_logic;
         my_address : OUT  std_logic_vector(31 downto 0);
         my_in_data : IN  std_logic_vector(31 downto 0);
         my_out_data : OUT  std_logic_vector(31 downto 0);
         my_wr : OUT  std_logic
        );
    END COMPONENT;
    
    
   
   type vec_32_array is array(0 to nodes - 1) of std_logic_vector(31 downto 0);
   
   --Inputs
   signal in_address : vec_32_array := (others => (others => '0'));
   signal in_data : vec_32_array := (others => (others => '0'));
   signal in_wr : std_logic_vector(0 to nodes - 1) := (others => '0');
   signal my_in_data : vec_32_array := (others => (others => '0'));

 	--Outputs
   signal out_address : vec_32_array;
   signal out_data : vec_32_array;
   signal out_wr : std_logic_vector(0 to nodes - 1);
   signal my_address : vec_32_array;
   signal my_out_data : vec_32_array;
   signal my_wr : std_logic_vector(0 to nodes - 1);
   
   signal clk: std_logic;
   
   -- No clocks detected in port list. Replace clk below with 
   -- appropriate port name 
 
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   
   chain_gen: for I in 0 to nodes - 1 generate
   
   first_node: if I=0 generate
 
      link0: Link generic map (num_cells => 13)

           PORT MAP (
                in_address => in_address(0),
                in_data => in_data(0),
                in_wr => in_wr(0),
                out_address => out_address(0),
                out_data => out_data(0),
                out_wr => out_wr(0),
                my_address => my_address(0),
                my_in_data => my_in_data(0),
                my_out_data => my_out_data(0),
                my_wr => my_wr(0)
           );
           
     end generate first_node;
           
   other_nodes: if I>0 generate
      
      linkX: Link
      
            generic map (num_cells => 7)
            
            PORT MAP (

                in_address => out_address(I-1),
                in_data => out_data(I-1),
                in_wr => out_wr(I-1),
                out_address => out_address(I),
                out_data => out_data(I),
                out_wr => out_wr(I),
                my_address => my_address(I),
                my_in_data => my_in_data(I),
                my_out_data => my_out_data(I),
                my_wr => my_wr(I)
           );
      end generate other_nodes;
      
   end generate chain_gen;


           -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	
      
      -- Initialization mode
      
      wait for clk_period*10;
      
      -- 
      for i in 1 to 64 loop
      
         in_address(0) <= std_logic_vector(to_unsigned(i,32));
         
         wait for clk_period * 10;
      
      end loop;

      -- insert stimulus here 

      wait;
   end process;

END;
