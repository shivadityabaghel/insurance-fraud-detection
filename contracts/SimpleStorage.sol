pragma solidity >=0.4.22 <0.9.0;

contract SimpleStorage {

    uint256 id;

    // Insurance policy function
    mapping(address => uint256) insurancePolicy;

    function set(uint256 _x) public {
        id = _x;
    }

    function get() public view returns (uint256) {
        return id;
    }

    // Function to buy insurance policy
    function buyInsurance() public payable {
        insurancePolicy[msg.sender] = msg.value;
    }

    // Function to claim insurance
    function claimInsurance() public {
        require(insurancePolicy[msg.sender] > 0, "You don't have an insurance policy.");
        uint256 amountToClaim = insurancePolicy[msg.sender];
        insurancePolicy[msg.sender] = 0;
        payable(msg.sender).transfer(amountToClaim);
    }
}
