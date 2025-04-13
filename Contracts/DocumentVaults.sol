// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVault {
    struct Document {
        string ipfsCID;
        string fileHash;
        address uploader;
        uint256 timestamp;
    }
    
    Document[] public documents;
    
    event DocumentAdded(uint256 docId, string ipfsCID, string fileHash, address uploader, uint256 timestamp);
    
    function addDocument(string calldata ipfsCID, string calldata fileHash) public {
        uint256 docId = documents.length;
        documents.push(Document(ipfsCID, fileHash, msg.sender, block.timestamp));
        emit DocumentAdded(docId, ipfsCID, fileHash, msg.sender, block.timestamp);
    }
    
    function getDocument(uint256 docId) public view returns (Document memory) {
        require(docId < documents.length, "Document does not exist");
        return documents[docId];
    }
}