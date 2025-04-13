// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVault {
    // The government address is set as the deployer (for demo)
    address public government;

    constructor() {
        government = msg.sender;
    }

    // Each document record
    struct Document {
        string ipfsCID;    // Document stored on IPFS
        string fileHash;   // Document file hash (e.g., SHA256)
        address uploader;  // Unique user address
        uint256 timestamp; // Time of document addition
        bool verified;     // Whether government verified it
    }
    
    // Map each uploader (user) to an array of their documents.
    mapping(address => Document[]) public documents;

    // Events triggered on actions
    event DocumentAdded(
        address indexed uploader,
        uint256 docId,
        string ipfsCID,
        string fileHash,
        uint256 timestamp
    );
    
    event DocumentVerified(
        address indexed uploader,
        uint256 docId,
        uint256 timestamp
    );

    // Modifier to restrict function calls to the government account.
    modifier onlyGovernment() {
        require(msg.sender == government, "Only government authorized");
        _;
    }

    /**
     * @dev Allows any user to add a document record.
     * @param _ipfsCID IPFS CID (content identifier) of the stored document.
     * @param _fileHash Cryptographic hash of the document.
     */
    function addDocument(string calldata _ipfsCID, string calldata _fileHash) external {
        documents[msg.sender].push(Document({
            ipfsCID: _ipfsCID,
            fileHash: _fileHash,
            uploader: msg.sender,
            timestamp: block.timestamp,
            verified: false
        }));
        
        uint256 docId = documents[msg.sender].length - 1;
        emit DocumentAdded(msg.sender, docId, _ipfsCID, _fileHash, block.timestamp);
    }

    /**
     * @dev Allows only the government to verify a document.
     * @param _uploader Address of the document uploader.
     * @param _docId Index of the document in the uploader's document array.
     */
    function verifyDocument(address _uploader, uint256 _docId) external onlyGovernment {
        require(_docId < documents[_uploader].length, "Document does not exist");
        Document storage doc = documents[_uploader][_docId];
        require(!doc.verified, "Document already verified");
        doc.verified = true;
        emit DocumentVerified(_uploader, _docId, block.timestamp);
    }

    /**
     * @dev Retrieves a document's details.
     * @param _uploader Address of the document owner.
     * @param _docId Index of the document.
     * @return The document struct.
     */
    function getDocument(address _uploader, uint256 _docId) external view returns (Document memory) {
        require(_docId < documents[_uploader].length, "Document does not exist");
        return documents[_uploader][_docId];
    }
}